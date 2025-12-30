###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9's 11th excrcise
import user_admin as ua

admin1 = ua.Admin("Subhajit","Hore","ADMIN-002")
admin1.describe_user()
admin1.privileges.add_privileges("Ban User")
admin1.show_admin_privileges()
