# -*- coding:utf-8 -*-

from django import forms
from CadVlan.messages import error_messages


class BlockRulesForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BlockRulesForm, self).__init__(*args, **kwargs)

    content = forms.CharField(
        label=u'Conteúdo',
        required=True,
        error_messages=error_messages,
        widget=forms.Textarea(
            attrs={
                'style': 'width: 300px',
                'rows': 10}))


class EnvironmentsBlockForm(forms.Form):

    def __init__(self, env_list, *args, **kwargs):
        super(EnvironmentsBlockForm, self).__init__(*args, **kwargs)
        self.fields['envs'].choices = (
            [
                (env['id'],
                 env["divisao_dc_name"] +
                    " - " +
                    env["ambiente_logico_name"] +
                    " - " +
                    env["grupo_l3_name"]) for env in env_list])

    envs = forms.ChoiceField(
        label=u'Ambiente',
        required=True,
        error_messages=error_messages)


class EnvironmentRules(forms.Form):

    name = forms.CharField(
        label="Nome da regra",
        required=True,
        error_messages=error_messages,
        widget=forms.TextInput(
            attrs={
                "style": "width: 300px;"}))


class ContentRulesForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContentRulesForm, self).__init__(*args, **kwargs)

    content = forms.CharField(
        label=u'Conteúdo',
        required=True,
        error_messages=error_messages,
        widget=forms.Textarea(
            attrs={
                'style': 'width: 300px',
                'rows': 7}))
    rule_content = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'order': ''}),
        label='',
        required=False,
        initial=0)


class DeleteForm(forms.Form):
    ids = forms.CharField(widget=forms.HiddenInput(), label='', required=True)
