# -*- coding:utf-8 -*-
'''
Title: CadVlan
Author: masilva / S2it
Copyright: ( c )  2012 globo.com todos os direitos reservados.
'''

from django.conf.urls.defaults import patterns, url
import settings

handler404 = 'CadVlan.Auth.views.handler404'
handler500 = 'CadVlan.Auth.views.handler500'

urlpatterns = patterns('',
    # CSS - JS
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)

# URL's Auth
urlpatterns += patterns('CadVlan.Auth.views',
    url('^[/]?$', 'login', name='',),
    url('^login[/]?$', 'login', name='login',),
    url('^logout[/]?$', 'logout', name='logout',),
    url('^home[/]?$', 'home', name='home',),
    url('^lost-pass[/]?$','lost_pass',name="home.lost.pass",),
    url('^change-pass[/]?$','change_password',name="home.change.pass",),
)

# URL's Script
urlpatterns += patterns('CadVlan.Script.views',
    url('^script/list[/]?$', 'list_all', name='script.list',),
    url('^script/delete[/]?$', 'delete_all', name='script.delete',),
    url('^script/form[/]?$', 'add_form', name='script.form',),
)

# URL's ScriptType
urlpatterns += patterns('CadVlan.ScriptType.views',
    url('^script-type/list[/]?$', 'list_all', name='script.type.list',),
    url('^script-type/delete[/]?$', 'delete_all', name='script.type.delete',),
    url('^script-type/form[/]?$', 'show_form', name='script.type.form',)
)

# URL's EquipAccess
urlpatterns += patterns('CadVlan.EquipAccess.views',
    url('^equip-access/search-list[/]?$', 'search_list', name='equip.access.search.list',),
    url('^equip-access/search-list/(?P<id_equip>\d+)[/]?$', 'search_list_param', name='equip.access.search.list.param',),
    url('^equip-access/form[/]?$','add_form', name='equip.access.form',),
    url('^equip-access/form/(?P<id_access>\d+)[/]?$','edit', name='equip.access.edit',),
    url('^equip-access/delete[/]?$','delete', name='equip.access.delete',),
)

# URL's Equipment Script
urlpatterns += patterns('CadVlan.EquipScript.views',
    url('^equip-script/list[/]?$', 'search_list', name='equip.script.search.list',),
    url('^equip-script/delete[/]?$','delete_all', name='equip.script.delete',),
    url('^equip-script/add[/]?$', 'ajax_add_form', name='equip.script.add.ajax',),
)

# URL's Equipment Interface
urlpatterns += patterns('CadVlan.EquipInterface.views',
    url('^equip-interface/list[/]?$', 'search_list', name='equip.interface.search.list',),
    url('^equip-interface/delete[/]?$','delete_all', name='equip.interface.delete',),
    url('^equip-interface/add/(?P<equip_name>[^/]+)[/]?$','add_form', name='equip.interface.form',),
    url('^equip-interface/edit/(?P<equip_name>[^/]+)/(?P<id_interface>\d+)[/]?$','edit_form', name='equip.interface.edit.form',),
    url('^equip-interface/addseveral/(?P<equip_name>[^/]+)[/]?$','add_several_forms', name='equip.interface.several.form',),
    url('^equip-interface/disconnect/(?P<id_interface>\d+)/(?P<back_or_front>\d+)/(?P<equip_name>[^/]+)/(?P<id_interf_edit>\d+)[/]?$','disconnect', name='equip.interface.disconnect',),
    url('^equip-interface/connect/(?P<id_interface>\d+)/(?P<front_or_back>\d+)[/]?$','connect', name='equip.interface.connect',),
)

# URL's Equipment
urlpatterns += patterns('CadVlan.Equipment.views',
    url('^equipment/autocomplete[/]?$', 'ajax_autocomplete_equips', name='equipment.autocomplete.ajax',),
    url('^equipment/list[/]?$', 'search_list', name='equipment.search.list',),
    url('^equipment/find[/]?$', 'ajax_list_equips', name='equipment.list.ajax',),
    url('^equipment/form[/]?$', 'equip_form', name='equipment.form',),
    url('^equipment/edit/(?P<id_equip>\d+)[/]?$', 'equip_edit', name='equipment.edit.by.id',),
    url('^equipment/modelo/(?P<id_marca>\d+)[/]?$', 'ajax_modelo_equip', name='equipment.modelo.ajax',),
    url('^equipment/marca[/]?$', 'ajax_marca_equip', name='equipment.modelo.ajax',),
    url('^equipment/modelo-form[/]?$', 'modelo_form', name='equipment.modelo.form',),
    url('^equipment/marca-form[/]?$', 'marca_form', name='equipment.marca.form',),
    
)

# URL's Environment
urlpatterns += patterns('CadVlan.Environment.views',
    url('^environment/list[/]?$', 'list_all', name='environment.list',),
    url('^environment/ambiente-logico[/]?$', 'insert_ambiente_logico', name='environment.insert.ambiente.logico',),
    url('^environment/grupo-l3[/]?$', 'insert_grupo_l3', name='environment.insert.grupo.l3',),
    url('^environment/divisao-dc[/]?$', 'insert_divisao_dc', name='environment.insert.divisao.dc',),
    url('^environment/form[/]?$', 'insert_ambiente', name='environment.form',),
    url('^environment/form/(?P<id_environment>\d+)[/]?$', 'edit', name='environment.edit',),
)

# URL's Vlans
urlpatterns += patterns('CadVlan.Vlan.views',
    url('^vlan/autocomplete[/]?$', 'ajax_autocomplete_vlans', name='vlan.autocomplete.ajax',),
    url('^vlan/get/(?P<id_vlan>\d+)[/]?$', 'list_by_id', name='vlan.list.by.id',), 
    url('^vlan/list[/]?$','search_list', name='vlan.search.list',),
    url('^vlan/find[/]?$','ajax_list_vlans', name='vlan.list.ajax',),
    url('^vlan/form[/]?$','vlan_form',name='vlan.form',), 
    url('^vlan/aclfilename[/]?$', 'ajax_acl_name_suggest', name='ajax.vlan.acl.file.name',),
    url('^vlan/edit/(?P<id_vlan>\d+)[/]?$','vlan_edit',name='vlan.edit.by.id',),
    url('^vlan/validate-acl[/]?$','ajax_validate_acl',name='ajax.vlan.acl.validate',),
)

# URL's Network
urlpatterns += patterns('CadVlan.Net.views',
    url('^network/form[/]?$', 'add_network_form', name='network.form',),
    url('^network/edit/rede_ipv4/(?P<id_net>\d+)[/]?$', 'edit_network4_form', name='network.edit.by.id.rede.ipv4',),
    url('^network/edit/rede_ipv6/(?P<id_net>\d+)[/]?$', 'edit_network6_form', name='network.edit.by.id.rede.ipv6',),
    url('^network/form/(?P<id_vlan>\d+)[/]?$', 'vlan_add_network_form', name='network.form.vlan',),
    url('^network/get/ip4/(?P<id_net>\d+)[/]?$', 'list_netip4_by_id', name='network.ip4.list.by.id',),
    url('^network/get/ip6/(?P<id_net>\d+)[/]?$', 'list_netip6_by_id', name='network.ip6.list.by.id',),
    url('^network/ip4/(?P<id_net>\d+)[/]?$','insert_ip4',name="network.insert.ip4",),
    url('^network/ip6/(?P<id_net>\d+)[/]?$','insert_ip6',name="network.insert.ip6",),
    url('^network/edit/ip4/(?P<id_net>\d+)/(?P<id_ip4>\d+)[/]?$','edit_ip4',name='network.edit.ip4',),
    url('^network/edit/ip6/(?P<id_net>\d+)/(?P<id_ip6>\d+)[/]?$','edit_ip6',name='network.edit.ip6',),
    url('^network/delete/(?P<id_net>\d+)/ip4[/]?$','delete_ip4',name='network.delete.ip4',),
    url('^network/delete/ip6/(?P<id_net>\d+)[/]?$','delete_ip6',name='network.delete.ip6',),
    url('^network/delete/ip6byequip/(?P<id_ip>\d+)/(?P<id_equip>\d+)[/]?$','delete_ip6_of_equip',name='network.delete.ip6.of.equip',),
    url('^network/delete/ip4byequip/(?P<id_ip>\d+)/(?P<id_equip>\d+)[/]?$','delete_ip4_of_equip',name='network.delete.ip4.of.equip',),
    url('^network/insert/ip4byequip/(?P<id_net>\d+)/(?P<id_equip>\d+)[/]?$','insert_ip4_by_equip',name='network.insert.ip4.of.equip',),
    url('^network/insert/ip6byequip/(?P<id_net>\d+)/(?P<id_equip>\d+)[/]?$','insert_ip6_by_equip',name='network.insert.ip6.of.equip',),
)

# URL's Option Vip
urlpatterns += patterns('CadVlan.OptionVip.views',
    url('^option-vip/list[/]?$', 'list_all', name='option-vip.list',),
    url('^option-vip/delete[/]?$', 'delete_all', name='option-vip.delete',),
    url('^option-vip/form[/]?$', 'add_form', name='option-vip.form',),
    url('^option-vip/form/(?P<id_optionvip>\d+)[/]?$', 'edit_form', name='option-vip.edit',),
)