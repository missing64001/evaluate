




window.onload=function(){
    var span = $('.get_user_group')
    var sc = span.next()
    span.parent().parent().parent().html('')

    var url = window.location.href.split('/')
    var num = url[url.length-3]
    var type = url[url.length-4]

    if (type == 'investreport' |  type =='bankreport'){
      
    
      var input = $('<form enctype="multipart/form-data" action="/admin/institution/save_reportback/" method="post" id="reportback_form" class="form-horizontal" novalidate="">\
            <div class="control-group form-row field-will "><div><div class="control-label"><label for="id_will">意向:</label></div><div class="controls"><select name="will" id="id_will"><option value="" selected="">---------</option><option value="1">有意向</option><option value="2">无意向</option></select></div></div></div>\
            <div class="control-group form-row field-type "><div><div class="control-label"><label for="id_type">选择反馈类别:</label></div><div class="controls"><select name="type" id="id_type"><option value="" selected="">---------</option><option value="1">对企业进一步了解</option><option value="2">与孵化器进一步协调</option></select></div></div></div>\
            <div class="control-group form-row field-note "><div><div class="control-label"><label for="id_note">反馈内容:</label></div><div class="controls"><textarea name="note" cols="40" id="id_note" rows="10" class="vLargeTextField"></textarea></div></div></div>\
            <div style="margin-top: 20px;"><button type="submit" class="btn btn-high btn-info  name="_save">提交</button></div></form>')




      input.append($('<input type="hidden" name="csrfmiddlewaretoken" value="'+ $("input:first").val()+'">'))
      input.append($('<input type="hidden" name="report_type" value="'+type+'">'))
      input.append($('<input type="hidden" name="report_id" value="'+num+'">'))

      $('div.inner-right-column').html(input)
      $('div.inner-right-column').css("width","480px")
      $('div.inner-center-column').css("margin-right","500px")



      var item1 = $("<div class='xx' ><a href='/admin/institution/companyinfo/"+ type + "/" + num +"/change/'>主要信息</a></div>")
      item1.css({"fontSize":"22px","margin":"20px",'display':'inline-block'})
      var content = $("#content").before(item1)

      var item1 = $("<div class='xx' ><a href='/admin/institution/"+ type + "/" + num +"/change/'>报告详情</a></div>")
      item1.css({"fontSize":"22px","margin":"20px",'display':'inline-block'})
      var content = $("#content").before(item1)
    }
}


// <div class="control-group form-row field-companyInfo "><div><div class="control-label"><label for="id_companyInfo">企业:</label></div><div class="controls"><div class="related-widget-wrapper"><select name="companyInfo" id="id_companyInfo"><option value="" selected="">---------</option><option value="1">c1</option><option value="2">c2</option><option value="3">c3</option><option value="4">c4</option><option value="5">c5</option></select><a class="related-widget-wrapper-link change-related" id="change_id_companyInfo" data-href-template="/admin/company/companyinfo/__fk__/change/?_to_field=id&amp;_popup=1" title="更改选中的一、基本信息"><img src="/static/admin/img/icon-changelink.svg" alt="修改"></a><a class="related-widget-wrapper-link add-related" id="add_id_companyInfo" href="/admin/company/companyinfo/add/?_to_field=id&amp;_popup=1" title="增加另一个 一、基本信息"><img src="/static/admin/img/icon-addlink.svg" alt="增加"></a></div></div></div></div>
// <div class="control-group form-row field-item "><div><div class="control-label"><label for="id_item">减分项:</label></div><div class="controls"><select name="item" id="id_item"><option value="" selected="">---------</option><option value="1">房屋信息通报</option><option value="2">经营者社会评价</option><option value="3">其他</option></select></div></div></div>












