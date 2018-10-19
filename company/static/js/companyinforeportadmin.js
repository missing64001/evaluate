window.onload=function(){
    var select = $('select.ms')
    select.change(function(event){
        tis = $(this)
        var opt = tis.children("option:selected")

        // alert(opt.val() + tis.attr('cid'))
        data={"cid":tis.attr("cid"),"type":tis.attr("type"),"opt":opt.val(),"csrfmiddlewaretoken":$("input:first").val()}
        post('/admin/institution/createcompanyreport/', data)
    })
}


function post(URL, PARAMS) {        
    var temp = document.createElement("form");        
    temp.action = URL;        
    temp.method = "post";        
    temp.style.display = "none";
    PARAMS =PARAMS ==null? {}:PARAMS;       
    for (var x in PARAMS) {        
        var opt = document.createElement("textarea");        
        opt.name = x;        
        opt.value = PARAMS[x];        
        // alert(opt.name)        
        temp.appendChild(opt);        
    }        
    document.body.appendChild(temp);        
    temp.submit();        
    return temp;        
} 