from django.apps import apps
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.test import TestCase

# Models di prova, sostituirli con i propri.
from core.models import CustomUser, Sex


class PermissionTests(TestCase):
    group_list = ['amministratore', 'utente']
    admin_permission_list = [
        ['can_view_control_panel', 'index_admin'],
        ['can_edit_users', 'edit_user'],
        ['can_view_user', 'view_user']
    ]
    user_permission_list = [
        ['can_view_user_panel', 'index_user'],
        ['can_edit_profile', 'edit_profile', ],
        ['can_view_profile', 'view_profile']
    ]

    def create_groups(self, list):
        try:
            for i in list:
                if not Group.objects.filter(name=str(i)).exists():
                    Group.objects.create(name=str(i))
            return Group.objects.all().name
        except Exception as e:
            return e

    def set_permission_to_group(self, permission, group):
        group = Group.objects.get(name=str(group))
        group.permissions.add(Permission.objects.get(name=str(permission)))
        return str(group.name) + ' - ' + Permission.objects.get(Q(codename=(permission)) | Q(name=str(permission))).name

    def get_content_types(self, app_label, model):
        try:
            return ContentType.objects.get(app_label=str(app_label), model=str(model))
        except Exception as e:
            print(e)
            return e

    def create_permission(self, permission, app_label, model):
        try:
            for i in permission:
                Permission.objects.get_or_create(codename=str(i[0]), name=str(i[1]),
                                                 content_type=ContentType.objects.get(app_label=str(app_label),
                                                                                      model=str(model)))
            return Permission.objects.all().name
        except Exception as e:
            return e

    def set_group_to_user(self, group, user, app_label, model):
        user = apps.get_model(app_label=str(app_label), model_name=str(model)).objects.get(username=str(user))
        group = Group.objects.get(name=str(group))
        group.user_set.add(user)
        print(user)
        return str(group.name) + ' - ' + str(user)

    def generate_permissions_and_groups(self, permissions, groups, app_label, model):
        return self.create_groups(groups), self.create_permission(permissions, app_label, model)

    ########################## TEST DEI METODI ###############################################

    def testGeneratePermissionsAndGroups(self):
        self.assertTrue(self.generate_permissions_and_groups(
            permissions=self.admin_permission_list,
            groups=self.group_list,
            app_label='core',
            model='CustomUser')
        )

    def testCreateGroups(self):
        self.assertTrue(self.create_groups(self.group_list))

    def testCreatePermission(self):
        self.assertTrue(
            self.create_permission(permission=self.admin_permission_list, app_label='core', model='CustomUser'))
        self.assertTrue(
            self.create_permission(permission=self.user_permission_list, app_label='core', model='CustomUser'))

    def testSetPermissionsToGroup(self):
        self.assertTrue(self.create_groups(self.group_list))
        self.assertTrue(
            self.create_permission(permission=self.admin_permission_list, app_label='core', model='CustomUser'))
        self.assertTrue(
            self.create_permission(permission=self.user_permission_list, app_label='core', model='CustomUser'))
        self.assertTrue(self.set_permission_to_group('index_admin', 'amministratore'))

    def testGetContentTypes(self):
        self.assertTrue(self.get_content_types('core', 'CustomUser'))

    def testSetGroupToUser(self):
        Sex.objects.create(sex='Uomo')
        CustomUser.objects.create(
            username='g.panarosa',
            password='provatesting',
            email='panarosagaetano@gmail.com',
            first_name='Gaetano',
            last_name='Panarosa',
            phone='3427749283',
            address='Via Ugo Foscolo 148',
            date_of_birth='1992-04-14',
            town='Mola di Bari',
            codice_fiscale='PNRGTN92D14F280M',
            sex=Sex.objects.get(sex='Uomo')
        )
        self.assertTrue(self.create_groups(self.group_list))
        self.assertTrue(
            self.create_permission(permission=self.admin_permission_list, app_label='core', model='CustomUser'))
        self.assertTrue(
            self.create_permission(permission=self.user_permission_list, app_label='core', model='CustomUser'))
        self.assertTrue(self.set_permission_to_group('index_admin', 'amministratore'))
        self.assertTrue(
            self.set_group_to_user(group='amministratore', user='g.panarosa', app_label='core', model='CustomUser'))
