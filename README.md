Bu videodan çalışıyorum: https://youtu.be/Kfc-PBtLrss?t=2162 
Oluşturduğu formları parçalı olarak templates/index'e gönderiyor ama ben yapınca ayrıştırılamıyor diye hata veriyor.

ContactForm\Home\templates\home\index.html, error at line 169
Error during template rendering
Could not parse the remainder: '% form.name %' from '% form.name %'

Sorun çözüldü:
{{% form.name %}} yanlış,

doğrusu : {{ form.name }}