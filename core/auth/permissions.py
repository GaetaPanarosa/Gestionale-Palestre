'''
Classe per la gestione dei permessi e gruppi di Django.
Permette la creazione e assegnazione degli stessi ad un model o utente di riferimento.
A partire dalla versione 3.0 di Django, dove sono stati inseriti degli script di check del sistema,
questa classe necessita dell'inserimento nel file settings.py della seguente variabile:
SILENCED_SYSTEM_CHECKS = ["models.E005"]
'''
from django.apps import apps
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


class CustomManagement():
    '''
        Questo metodo permette di creare automaticamente gruppi e permessi passando la lista di permessi,
        la lista dei gruppi, l'app django di riferimento e il model di riferimento.
        -------
        permissions = Lista di permessi type: Array[Array[str,str]]
        groups = Lista di gruppi type: Array[str]
        app_label = nome dell'applicazione django type: str
        model = nome del model di riferimento type: str
        -------
        formato permissions = [
            ['can_create_profile','create_profile'],
            ['can_view_profile','view_profile'],
            ['can_edit_profile','edit_profile'],
            ['can_delete_profile','delete_profile'],
            ...,
        ]
        formato groups = ['group_name1','group_name2',...]
        formato app_label = 'core'
        formato model = 'User'

    '''

    def generate_permissions_and_groups(self, permissions, groups, app_label, model):
        return self.create_groups(groups), self.create_permission(permissions, app_label, model)

    ##################################################################################################################

    '''
        Questo metodo permette di recuperare il content type di un model in una determinata app django.
        Utile se si vogliono impostare manualmente dei permessi.
        -------
        app_label = nome dell'applicazione django type: str
        model = nome del model di riferimento type: str
        -------
        formato app_label = 'core'
        formato model = 'User'
    '''

    def get_content_types(self, app_label, model):
        try:
            return ContentType.objects.get(app_label=str(app_label).lower(), model=str(model).lower())
        except Exception as e:
            print(e)
            return e

    ##################################################################################################################

    '''
        Questo metodo permette di creare dei permessi attraverso la lettura di una lista di permessi, nome dell'app django di riferimento e il modello di riferimento.
        In caso esistano, non verranno modificati.
        ATTENZIONE:
        -------
        list = Lista di permessi type: Array[Array[str,str]]
        app_label = applicazione django type: str
        model = model a cui va applicato il permesso type:str
        -------
        formato list = [
            ['can_create_profile','create_profile'],
            ['can_view_profile','view_profile'],
            ['can_edit_profile','edit_profile'],
            ['can_delete_profile','delete_profile'],
            ...,
        ]
        formato app_label = 'core'
        formato model = 'User'
    '''

    def create_permission(self, permission, app_label, model):
        try:
            for i in permission:
                # Permission.objects.get_or_create(codename=str(i[0]).lower(), name=str(i[1]).lower(),
                #                                  content_type=ContentType.objects.get(app_label=str(app_label).lower(),
                #                                                                       model=str(model).lower()))
                Permission.objects.get_or_create(codename=str(i[0]), name=str(i[1]), content_type_id=2)
            return Permission.objects.all().name
        except Exception as e:
            print('Exception ', e)
            return e

    ##################################################################################################################
    '''
        Questo metodo permette di creare dei gruppi attraverso la lettura di una lista di gruppi.
        In caso esistano, non verranno modificati.
        -------
        list = Lista di gruppi type: Array[str]
        -------
        formato list = ['group_name1','group_name2',...]
    '''

    def create_groups(self, list):
        try:
            for i in list:
                if not Group.objects.filter(name=str(i)).exists():
                    Group.objects.create(name=str(i))
            return Group.objects.all().name
        except Exception as e:
            return e

    ##################################################################################################################

    '''
        Questo metodo permette di assegnare un permesso ad un gruppo di utenti.
        Nel caso in cui si vogliano assegnare più permessi allo stesso gruppo,
        basta iterare questo metodo con la lista di permessi creata e passare il nome del permesso.
        -------
        permission = codename o nome del permesso type: str
        group = nome del gruppo type: str
        --------
        formato permission = 'view_profile'
        formato group = 'utenti'
    '''

    def set_permission_to_group(self, permission, group):
        group = Group.objects.get(name=str(group))
        try:
            group.permissions.add(Permission.objects.get(name=str(permission[1]), codename=str(permission[0])))
            return str(group.name) + ' - ' + Permission.objects.get(
                Q(codename=(permission)) | Q(name=str(permission))).name
        except Exception as e:
            print('Exception: ', e)
            return e

    ##################################################################################################################

    '''
    Questo metodo permette di assegnare un utente ad un gruppo passandogli il nome del gruppo, l'username dell'utente,
    l'app django di riferimento e il model di riferimento.
    -------
    group = nome del gruppo type: str
    user = username dell'utente type: str
    app_label = applicazione django di riferimento type: str
    model = model di riferimento type: str
    -------
    '''

    def set_group_to_user(self, group, user, app_label, model):
        user = apps.get_model(app_label=str(app_label), model_name=model).objects.get(username=str(user))
        group = Group.objects.get(name=str(group))
        group.user_set.add(user)
        print(user)
        return str(group.name) + ' - ' + str(user)
