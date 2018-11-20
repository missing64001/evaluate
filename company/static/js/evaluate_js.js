



$(function(){
   var addslst = $('.inline-group .add-row>a')
   for (var i=0;i<addslst.length;i++){
        var a = $(addslst[i])
        a.text(a.text().replace('添加另一个','添加'))
   }
})



