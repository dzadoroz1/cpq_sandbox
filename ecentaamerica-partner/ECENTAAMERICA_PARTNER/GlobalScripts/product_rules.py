from Scripting import SqlDbType

def handle_simple_attribute_rules(model, Product):
    Trace.Write("Attribute_rules " + Product.Attr('Config Rules').SelectedValue.ValueCode)
    if not int(Product.Attr('Config Rules').SelectedValue.ValueCode):
        # Config Rules disabled
        Trace.Write("Attribute_rules Config Rules disabled")
        return

    base_sql_query = """
    SELECT *
    FROM TORO_ATTRIBUTE_RULES
    WHERE model = @model_name AND source_attr = @attribute_name
    """

    modelParam = SqlHelper.CreateParameter(model, "@model_name", SqlDbType.NVarChar)

    i = 0
    for attr in Product.Attributes:
        Trace.Write((i, 'loop attr.Name: ',  attr.Name))
        i += 1
        if attr.SelectedValue:
            sql_query = base_sql_query
            attributeNameParam = SqlHelper.CreateParameter(attr.Name, "@attribute_name", SqlDbType.NVarChar)

            # Build the LIKE conditions and parameters for each selected attribute value
            like_conditions = []
            parameters = [modelParam, attributeNameParam]

            for i, attr_value in enumerate(attr.SelectedValues):
                param_name = "@source_attribute_value{}".format(i) 
                like_conditions.append("source_attr_values LIKE CONCAT(CONCAT('%',{}), '%')".format(param_name))
                parameters.append(SqlHelper.CreateParameter(attr_value.ValueCode, param_name, SqlDbType.NVarChar))

            # Add the dynamic LIKE conditions to the SQL query
            if like_conditions:
                sql_query += " AND (" + " OR ".join(like_conditions) + ")"
            
            # Log the final query for debugging purposes
            Trace.Write("Final SQL Query: " + sql_query)

            # Execute the query with all parameters
            sql_res = SqlHelper.GetList(sql_query, *parameters)
			
            
            # Process the results
            if not sql_res:
                Trace.Write('empty query')
                continue
            for rule in sql_res:
                source_avc_list = [x.strip() for x in rule.source_attr_values.split(',')]

                # Loop through each attribute value
                for attr_value in source_avc_list:
                    dest_attr = Product.Attributes.GetByName(rule.dest_attr)
                    if dest_attr:
                        Trace.Write(dest_attr.Name)
                        if rule.action == 'DisallowAttr':
                            Trace.Write('Disallowing attribute: {}'.format(rule.dest_attr))
                            Product.DisallowAttr(rule.dest_attr)
                        elif rule.action == 'DisallowAttrValues':
                            Trace.Write(
                                'Disallowing attribute values for {}: {}'.format(rule.dest_attr, rule.dest_attr_values)
                            )
                            dest_avc_list = [x.strip() for x in rule.dest_attr_values.split(',')]
                            Product.DisallowAttrValues(rule.dest_attr, *dest_avc_list)
                        elif rule.action == 'SelectAttrValues':
                            dest_avc_list = [x.strip() for x in rule.dest_attr_values.split(',')]
                            for dest_avc in dest_attr.SelectedValues:
                                dest_avc_list.append(dest_avc.ValueCode)
                            Trace.Write(
                                'Selecting attribute values for {}: {}'.format(rule.dest_attr, dest_avc_list)
                            )
                            Product.SelectAttrValues(rule.dest_attr, *dest_avc_list)
                        elif rule.action == 'SetRequired':
                            Trace.Write('Setting attribute {} as required'.format(rule.dest_attr))
                            # Implement the required logic if necessary
                        else:
                            Trace.Write("Unknown action: {}".format(rule.action))
                    else:
                        Trace.Write("Destination attribute not found: {}".format(rule.dest_attr))
    # End attribute loop
