








$(function(){
    var z = $('div.inner-center-column')
    var s1 = $('#id_external_environment')
    // console.log(s1)
    var s2 = $('#id_products_and_market')
    var s3 = $('#id_technology_R_D')
    var s4 = $('#id_team')
    var csrf = $("input[name='csrfmiddlewaretoken']")

    var name = $('.readonly')
    if (name.length == 5){
        s1 = "<h2>校正评价：" +$(name[1]).text() + "</h2>"
        s2 = "<h2>校正评价：" +$(name[2]).text() + "</h2>"
        s3 = "<h2>校正评价：" +$(name[3]).text() + "</h2>"
        s4 = "<h2>校正评价：" +$(name[4]).text() + "</h2>"
    }
    name = $(name[0]).text()

    // console.log(name.count)
    // z.html('')
    
    $('div.control-label').parent().remove()

    var isocre1 = ""
    var isocre2 = ""
    var isocre3 = ""
    var isocre4 = ""

    if (parseInt($("input.isocre1").val())){
        isocre1 = "　　自评：" + $("input.isocre1").val() +"分"
    }
    if (parseInt($("input.isocre2").val())){
        isocre2 = "　　自评：" + $("input.isocre2").val() +"分"
    }
    if (parseInt($("input.isocre3").val())){
        isocre3 = "　　自评：" + $("input.isocre3").val() +"分"
    }
    if (parseInt($("input.isocre4").val())){
        isocre4 = "　　自评：" + $("input.isocre4").val() +"分"
    }
    form = $("#evaluationofenterprises_form")
    form.submit(function(e){
    return confirm('提交后数据不可更改\n请确认是否提交');
    });

    // z.append(csrf)
    if (s1.length){
        z.append($("<h1>"+name+"</h1>"))
        z.append($("<h2>企业所处外部环境"+isocre1+"</h2>"))
        z.append($("<h5>根据企业经营业务与政府优先发展的战略性优势产业契合度自评；</h5>"))
        z.append($("<h5>根据政府对企业所处行业政策利好情况自评；</h5>"))
        z.append($("<h5>根据主营产品所在市场竞争格局及自身竞争优势自评；</h5>"))
        z.append($("<h5>根据企业所处行业产能与集中度利好情况自评；</h5>"))
        z.append(s1)
        z.append($("<h2>企业主营产品及市场开拓"+isocre2+"</h2>"))
        z.append($("<h5>企业主营产品或服务及业务领域稳定性自评；</h5>"))
        z.append($("<h5>企业主营产品或服务在市场容量中份额自评；</h5>"))
        z.append($("<h5>企业主营产品或服务在未来市场预测的自评；</h5>"))
        z.append(s2)
        z.append($("<h2>企业核心技术及研发实力"+isocre3+"</h2>"))
        z.append($("<h5>企业核心技术创新性、技术所产阶段自评；</h5>"))
        z.append($("<h5>企业核心技术的自主研发能力自评；</h5>"))
        z.append($("<h5>企业研发团队能力、承担课题、专利等情况的自评；</h5>"))
        z.append(s3)
        z.append($("<h2>企业经营及管理团队"+isocre4+"</h2>"))
        z.append($("<h5>管理层学历状况、主要管理层在同行业从业经历、从业时间、管理经验、经营业绩及相关社会背景自评；</h5>"))
        z.append(s4)
        var seth5 = $('h5')
        seth5.css({'fontSize':'14px','fontWeight':'500','color':'#888','margin-left':'8px'})

        var seth2 = $('h2')
        seth2.css({'margin-top':'28px'})
    }

});



// window.onload=function(){
//     var z = $('div.inner-center-column')
//     var s1 = $('#id_external_environment')
//     // console.log(s1)
//     var s2 = $('#id_products_and_market')
//     var s3 = $('#id_technology_R_D')
//     var s4 = $('#id_team')
//     var csrf = $("input[name='csrfmiddlewaretoken']")

//     var name = $('.readonly').text()
//     // z.html('')
    
//     $('div.control-label').parent().remove()
//     // z.append(csrf)
//     if (s1.length){
//         z.append($("<h1>"+name+"</h1>"))
//         z.append($("<h2>企业所处外部环境</h2>"))
//         z.append($("<h5>根据企业经营业务与政府优先发展的战略性优势产业契合度自评；</h5>"))
//         z.append($("<h5>根据政府对企业所处行业政策利好情况自评；</h5>"))
//         z.append($("<h5>根据主营产品所在市场竞争格局及自身竞争优势自评；</h5>"))
//         z.append($("<h5>根据企业所处行业产能与集中度利好情况自评；</h5>"))
//         z.append(s1)
//         z.append($("<h2>企业主营产品及市场开拓</h2>"))
//         z.append($("<h5>企业主营产品或服务及业务领域稳定性自评；</h5>"))
//         z.append($("<h5>企业主营产品或服务在市场容量中份额自评；</h5>"))
//         z.append($("<h5>企业主营产品或服务在未来市场预测的自评；</h5>"))
//         z.append(s2)
//         z.append($("<h2>企业核心技术及研发实力</h2>"))
//         z.append($("<h5>企业核心技术创新性、技术所产阶段自评；</h5>"))
//         z.append($("<h5>企业核心技术的自主研发能力自评；</h5>"))
//         z.append($("<h5>企业研发团队能力、承担课题、专利等情况的自评；</h5>"))
//         z.append(s3)
//         z.append($("<h2>企业经营及管理团队</h2>"))
//         z.append($("<h5>管理层学历状况、主要管理层在同行业从业经历、从业时间、管理经验、经营业绩及相关社会背景自评；</h5>"))
//         z.append(s4)
//         var seth5 = $('h5')
//         seth5.css({'fontSize':'5px','fontWeight':'500','color':'#888','margin-left':'8px'})

//         var seth2 = $('h2')
//         seth2.css({'margin-top':'28px'})

//     }

//     // font-: 10px;
//     // font-weight: 800;
// }