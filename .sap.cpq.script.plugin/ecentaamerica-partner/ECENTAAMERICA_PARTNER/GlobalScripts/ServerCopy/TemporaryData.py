Bundle = {}
Bundle['Offer'] = 'Avaya OneCloud Public CCaaS'
Bundle['Bundles'] = ["Voice Bundle (Spoken)", "Voice Bundle (IXCC - Mar 2021)","Digital Only Bundle (IXCC - Dec 2020)", "(Voice plus) Digital Bundle (IXCC - Mar 2021)", "(Voice plus) Digital Bundle (Spoken)" ]

#########################################
##Bundle and it's list of capbilties
#########################################
bundleCapabilitiesList = {}
bundleCapabilitiesList['Voice Bundle (Spoken)'] = ['Business Voice','PSTN Voice', 'CC Desktop', 'CC Voice Media Client', 'Skills Based Routing', 'Operational Reporting - Inbound Voice', 'DTMF Interaction (Self Service)' , 'Compliance Recording','Screen Capture']
bundleCapabilitiesList['(Voice plus) Digital Bundle (Spoken)'] = ['Business Voice','PSTN Voice', 'CC Desktop', 'CC Voice Media Client', 'Skills Based Routing', 'Operational Reporting - Inbound Voice','Compliance Recording','Screen Capture','Email','Chat','Operational Reporting - Inbound Digital','DTMF Interaction (Self Service)','Quality Management']
bundleCapabilitiesList['Digital Only Bundle (IXCC - Dec 2020)'] = ['Email','Chat','CC Desktop','Attribute Matching','Journey Service','Operational Reporting - Inbound Digital']
bundleCapabilitiesList['Voice Bundle (IXCC - Mar 2021)'] = ['Business Voice','PSTN Voice', 'CC Desktop', 'CC Voice Media Client', 'Attribute Matching', 'Operational Reporting - Inbound Voice', 'DTMF Interaction (Self Service)' , 'Compliance Recording','Screen Capture','Operational Reporting - Inbound Digital']
bundleCapabilitiesList['(Voice plus) Digital Bundle (IXCC - Mar 2021)'] = ['Business Voice','PSTN Voice','Email','Chat','CC Desktop','CC Voice Media Client','Attribute Matching','Operational Reporting - Inbound Voice','Operational Reporting - Inbound Digital', 'DTMF Interaction (Self Service)']

#########################################
##Capability and it's list of eatures
#########################################
features = {}
features['Business Voice'] = ['Direct Inward Dialing / Direct Outward Dialing','Call Holds / Call Transfers','12 Party Conferencing','Class of Service Screening / Restrictions','Calling Name / Called Name']
features['PSTN Voice'] = ['Support for Voice as a Channel']
features['CC Desktop'] = ['Agent Desktop Workspaces with Extensible Widget Framework','Multiple Desktop Platforms','All Channel Active Sessions & Sessions "On-Hold"','All Channel Backlog with Ability to Cherry Pick Specific Sessions']
features['CC Voice Media Client'] = ['Voice Media Control / Anchoring','Multiple Desktop Platforms','IP Phone Control']
features['Skills Based Routing'] = ['Voice Media Control / Anchoring','Multiple Desktop Platforms','IP Phone Control']
features['Operational Reporting - Inbound Voice'] = ['Historical Reporting of Incoming Voice Calls','Realtime Dashboards to Supervisors of Incoming Voice Calls','Standard and Custom Reports']
features['DTMF Interaction (Self Service)'] = ['VXML / CCXML Interpretation Engine for IVR Scripts','Application Server to Run (Interpreted) IVR Scripts','Collection of DTMF Inputs to Traverse IVR Script / Menu Tree','Session Detail Records (SDRs) with Session Stats and Results','Final Results Available for Next Stage Routing of Voice Session']
features['Compliance Recording'] = ['GR/HA Redundant Realtime Voice Recorders','Encryption in Transit and at Rest for Recorded Sessions','Search, Retreive and Playback of Recordings','Content-driven CR Reports / Dashboards to Supervisors','90 Days of Cloud Storage for Call Recordings']
features['Screen Capture'] = ['Agents\' entire Desktop recorded including all Channel widgets','Encryption in Transit and at Rest for Recorded Sessions','Search, Retreive and Playback of Recordings','90 Days of Cloud Storage for Call Recordings']
features['Chat'] = ['Chat Session in Agent Desktop (Active and "On-Hold")','Ability to "Cherry Pick" Chats from Chat Queue / Backlog','Read, Reply, Forward Chat Sessions','Supervisor Review / Grade of Chat Replies']
features['Quality Management'] = ['GR/HA Redundant Realtime Voice Recorders','Encryption in Transit and at Rest for Recorded Sessions','Search, Retreive and Playback of Recordings','Content-driven CR Reports / Dashboards to Supervisors','90 Days of Cloud Storage for Call Recordings','Lesson Management','Coaching','Advanced Scorecards with automated scoring of questions on evaluation forms']
features['Email'] = ['Email Session in Agent Desktop (Active and "On-Hold")','Ability to "Cherry Pick" Emails from Email Queue / Backlog','Read, Reply, Forward Emails','Supervisor Review / Approve / Grade of Email Replies']
features['Attribute Matching'] = ['Match the customer with the best agent based on a rich set of attributes','Attributes List','Mapping Agent to List of Attributes for Said Agent']
features['Journey Service'] = ['Store events associated with customer journey in records','Storage and retreival API']
features['Operational Reporting - Inbound Digital'] = ['Historical Reporting of Incoming Voice and Digital Channels ','Realtime Dashboards to Supervisors of Incoming Voice and Digital Channels','Standard and Custom Reports']

#########################################
##Guided selling questions
#########################################
guidedSelling = []
list = {}
list['Bundle']= ['Digital Only Bundle (IXCC - Dec 2020)']
list['Questions'] = ['Number of Agents Handling Only 1 Digital Channel (Email, Chat, etc.)','Number of Agents Handling Only 2 Digital Channel (Email, Chat, etc.)']
guidedSelling.append(list)
list = {}
list['Bundle'] = ['Voice Bundle (IXCC - Mar 2021)'] 
list['Questions'] = ['Number of Agents Handling Only Voice Calls']
guidedSelling.append(list)
list = {}
list['Bundle'] = ['(Voice plus) Digital Bundle (IXCC - Mar 2021)']
list['Questions'] = ['Number of Agents Handling Voice as well as Handling Digital Channels']
guidedSelling.append(list)