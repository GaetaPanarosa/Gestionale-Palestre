from core.auth.permissions import *
from core.auth.views import *

group_list = ['administrator', 'user', 'trainer', 'editor']

admin_permission_list = [
    ['can_view_control_panel', 'index_admin'],
    ['can_edit_users', 'edit_user'],
    ['can_view_user', 'view_user'],
    ['can_view_prenotations', 'view_prenotations'],
    ['can_edit_prenotations', 'edit_prenotations'],
    ['can_dismiss_prenotation', 'dismiss_prenotations'],
]
user_permission_list = [
    ['can_view_user_panel', 'index_user'],
    ['can_edit_profile', 'edit_profile', ],
    ['can_view_profile', 'view_profile']
]

trainer_permission_list = [
    ['can_view_trainer_panel', 'index_trainer'],
    ['can_edit_profile', 'edit_profile', ],
    ['can_view_profile', 'view_profile'],
    ['can_view_his_course', 'view_his_course_list']
]

editor_permission_list = [
    ['can_view_cms', 'index_cms'],
    ['can_edit_cms', 'edit_cms'],
    ['can_delete_cms', 'delete_cms']
]

management = CustomManagement()

management.create_groups(list=group_list)
print('Gruppi creati e/o aggiornati')

management.create_permission(permission=admin_permission_list, app_label='core', model='CustomUser')
management.create_permission(permission=user_permission_list, app_label='core', model='CustomUser')
management.create_permission(permission=trainer_permission_list, app_label='core', model='CustomUser')
management.create_permission(permission=editor_permission_list, app_label='core', model='CustomUser')

print('Permessi creati e/o aggiornati')

for perm in admin_permission_list:
    management.set_permission_to_group(permission=perm, group='administrator')

for perm in user_permission_list:
    management.set_permission_to_group(permission=perm, group='user')

for perm in trainer_permission_list:
    management.set_permission_to_group(permission=perm, group='trainer')

for perm in editor_permission_list:
    management.set_permission_to_group(permission=perm, group='editor')

