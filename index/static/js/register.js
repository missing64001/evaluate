


var option1 = '<label for="id_password" class="control-label required">企业名称:</label> <input type="text" name="name" required />\
                    <label for="id_password" class="control-label required">所属孵化器:</label> \
                    <select name="incubator" style="width: 292px">\
                        <option value="1">企业用户</option>\
                        <option value="2">孵化器管理团队</option>\
                        <option value="3">平台管理团队</option>\
                        <option value="4">金融机构</option>\
                    </select>\
                    <label for="id_password" class="control-label required">统一社会信用代码:</label> <input type="text" name="credit_code" required />\
                    <label for="id_password" class="control-label required">企业电话:</label> <input type="text" name="phone" required />\
                    <label for="id_password" class="control-label required">上传营业执照:<input type="file" name="business_license_pic" required>'

var option2 = '<label for="id_password" class="control-label required">孵化器名称:</label> <input type="text" name="name" required />\
                  <label for="id_password" class="control-label required">孵化器电话:</label> <input type="text" name="phone" required />'


var option3 = '<label for="id_password" class="control-label required">机构名称:</label> <input type="text" name="name" required />\
                  <label for="id_password" class="control-label required">机构电话:</label> <input type="text" name="phone" required />'










window.onload=function(){
    var input = $('select.s1');
    input.change(function(event){
    var s1 = $(event.target).val()
    var doption = $('div.option')
    if (s1 == 1){
        doption.html(option1)
    }
    else if(s1 == 2){
        doption.html(option2)
    }
    else if(s1 == 3 | s1 == 4){
        doption.html(option3)
    }

    });

}



