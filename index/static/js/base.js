// 全局change_list的js
// 功能1 调整breadcrumb 删除change_view模板中的 ‘另一个’
// 


$(function(){
    
    // // 111 设置 首页的链接显示 不需要设置了
    // var global_group = $('#global_group').attr('name')
    // var url = location.pathname

    // //设置 平台管理员的
    // if (global_group == 'super' & url == '/admin/'){
    //     console.log('super1')
    //     var cm_tbody = $('#content-main tbody')
    //     var cm_tbody_tr = $('#content-main tbody:eq(0) tr')
    //     $(cm_tbody[0]).html($(cm_tbody_tr[0]))


    //     cm_tbody_tr = $('#content-main tbody:eq(3) tr:gt(1)')
    //     cm_tbody_tr.remove()

    //     $('#content-main tbody .addlink').parent().remove()
    // }

    // // 设置 企业用户
    // else if (global_group == '企业用户' & url == '/admin/'){
    //     $('#content-main tbody:lt(2) .changelink').parent().next().remove()
    //     $('#content-main tbody:eq(0) tr:gt(0):lt(8)').remove()
    // }

    // // 设置 孵化器用户
    // else if (global_group == '孵化器用户' & url == '/admin/'){
    //     $('#content-main tbody:lt(3) .changelink').parent().next().remove()
    //     $('#content-main tbody:eq(0) tr:gt(0):lt(9)').remove()
    // }

    // // 设置 机构用户
    // else if (global_group == '机构用户' & url == '/admin/'){
    //     $('#content-main tbody:lt(3) .changelink').parent().next().remove()
    //     $('#content-main tbody:eq(0) tr:gt(0)').remove()
    //     $('#content-main tbody:eq(1) tr:odd').remove()
    // }



    // 222 设置侧边栏和导航栏的数据
    var lis = $('ul.breadcrumb>li')
    // console.log(lis.length)
    if (lis.length > 2){
        var activeli = $('#left-nav>ul>li.active')
        if (activeli.children('a').length){
            // console.log(activeli.children('a').length)
            $(lis[1]).children('a').attr('href',activeli.children('a').attr('href'))
            $(lis[1]).children('a').text(activeli.children('a').text())
        }

    }
    if (lis.length == 4){
        var activeli = $('#left-nav>ul>li.active li.active')
        if (activeli.children('a').length){
            // console.log(activeli.children('a').length)
            $(lis[2]).children('a').attr('href',activeli.children('a').attr('href'))
            $(lis[2]).children('a').text(activeli.children('a').text())
        }

    }

    var activeliz = $('#left-nav>ul>li.active li.active')
    // console.log($(lis[2]).text())
    if (activeliz.children('a').text() == '校正评价' & $(lis[2]).text() == '自主评价'){
        $(lis[2]).text('校正评价')
    }
    if (activeliz.children('a').text() == '孵化器数据统计' & $(lis[2]).text() == '孵化器'){
        $(lis[2]).text('孵化器数据统计')

        var downbutton = $('<button class="btn btn-success" style="margin-bottom:10px;">导出全部数据</button>')
        downbutton.bind("click",function(event){
            window.location.href='/download_data'
        })



        $('#content').before(downbutton)
    }
    if (activeliz.children('a').text() == '企业数据统计' & $(lis[2]).text() == '一、基本信息'){
        $(lis[2]).text('企业数据统计')
    }



    // 333 设置 /admin/auth/user/res_in 页面的breadcrumb
    if (url == "/admin/auth/user/res_in"){
        console.log('xxxxxxxxxx')
        var b = '<ul class="breadcrumb">\
                      <li><a href="/admin/">首页</a>\
                        <span class="divider">»</span></li>\
                      <li>\
                        <a href="/admin/auth/user/">账号管理\
                            </a>\
                        <span class="divider">»</span></li>\
                      <li class="active">增加 孵化器/机构用户</li>\
                    </ul>'

        $('ul.breadcrumb').html(b)
    }

})


$(function(){
    // 444 
   var addslst = $('.inline-group .add-row>a')
   for (var i=0;i<addslst.length;i++){
        var a = $(addslst[i])
        a.text(a.text().replace('添加另一个','添加'))
   }




   // 555 删除不需要保存的 保存选项
   isremove = $('#global_is_close_save').attr('name')
   console.log(isremove)
   if (isremove == '1'){
        $('.save-box').remove()
   }
   
})


