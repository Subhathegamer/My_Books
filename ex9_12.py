###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp9's 12th excrcise
from user import User
from admin import Admin
from privileges import Privileges


admin3 = Admin("Subhajit","Hore","ADMIN-002")
admin3.greet_user()
admin3.privileges.add_privileges("ADD POST")
admin3.privileges.add_privileges("REMOVE POST")
admin3.privileges.add_privileges("EDIT POST")
admin3.privileges.add_privileges("ADD USER")
admin3.privileges.add_privileges("BAN USER")
admin3.show_admin_privileges()