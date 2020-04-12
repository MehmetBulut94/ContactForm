

________________________________________________________________________
1.hata: ContactForm\Home\templates\home\index.html, error at line 169
Error during template rendering
Could not parse the remainder: '% form.name %' from '% form.name %'

Sorun çözüldü:
{{% form.name %}} yanlış,

doğrusu : {{ form.name }}
