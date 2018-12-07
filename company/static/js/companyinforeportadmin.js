window.onload=function(){
    var select = $('select.ms')
    select.change(function(event){
        tis = $(this)
        var opt = tis.children("option:selected")

        // alert(opt.val() + tis.attr('cid'))
        data={"cid":tis.attr("cid"),"type":tis.attr("type"),"opt":opt.val(),"csrfmiddlewaretoken":$("input[name='csrfmiddlewaretoken']").val()}
        post('/admin/institution/createcompanyreport/', data)
    })
}

function createcompanyreport(tt) {
    tis = $(tt)
    // console.log(tis)
    data={"cid":tis.attr("cid"),"type":tis.attr("_type"),"opt":tis.attr("value"),"csrfmiddlewaretoken":$("input[name='csrfmiddlewaretoken']").val()}
    // console.log(data)
    post('/admin/institution/createcompanyreport/', data)
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