// 全局change_list的js
// 功能1 调整breadcrumb 删除change_view模板中的 ‘另一个’
// 


$(function(){
    var lis = $('ul.breadcrumb>li')
    // console.log(lis.length)


    if (lis.length > 2){
        var activeli = $('#left-nav>ul>li.active')
        // console.log(activeli.children('a').attr('href'))
        // console.log(activeli.children('a').text())
        $(lis[1]).children('a').attr('href',activeli.children('a').attr('href'))
        $(lis[1]).children('a').text(activeli.children('a').text())
    }
    if (lis.length == 4){
        var activeli = $('#left-nav>ul>li.active li.active')
        // console.log(activeli.children('a').attr('href'))
        // console.log(activeli.children('a').text())
        $(lis[2]).children('a').attr('href',activeli.children('a').attr('href'))
        $(lis[2]).children('a').text(activeli.children('a').text())
    }

    var activeliz = $('#left-nav>ul>li.active li.active')
    console.log($(lis[2]).text())
    if (activeliz.children('a').text() == '校正评价' & $(lis[2]).text() == '自主评价'){
        $(lis[2]).text('校正评价')
    }

})


$(function(){
   var addslst = $('.inline-group .add-row>a')
   for (var i=0;i<addslst.length;i++){
        var a = $(addslst[i])
        a.text(a.text().replace('添加另一个','添加'))
   }
})


