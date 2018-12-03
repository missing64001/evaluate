function verify() {
    var input = $('#inputbrowsers')
    console.log(input.val())
    if (input.val()){

        return true
    }
    else{

        alert('请填写年份')
        return false
    }
}


// function yearchange() {
//     var input = $('#inputbrowsers')
//     var year = input.val()
//     window.location.href="/admin/company/balance/?year=" + year
//     // console.log(year)
// }

function deldata() {
    var input = $('#inputbrowsers')
    var year = input.val()
    window.location.href="/admin/company/deldata/?year=" + year + '&model=balance' 
    // console.log(year)
}


window.onload=function(){
    var input = $('input');
    input.on('input propertychange',function(event){
        var jthis = $(event.target);
        var name = jthis.attr("name");
        
        n1 = name[0]
        n2 = name.slice(1)
        jthis.val(jthis.val().replace(",",""))


        if (n1 == 'd')
        {
            if(n2<17)
            {
                d17()
                d38()
            }
            else if(n2==24 | n2==25)
            {
                d26()
                d28()
                d37()
                d38()
            }
            else if(n2==27)
            {
                d28()
                d37()
                d38()
            }
            else if(n2==29|n2==32|n2==34|n2==36){
                d37()
                d38()
            }
        }
        else if (n1 == 'e')
        {
            if(n2<17)
            {
                e17()
                e38()
            }
            else if(n2==24 | n2==25)
            {
                e26()
                e28()
                e37()
                e38()
            }
            else if(n2==27)
            {
                e28()
                e37()
                e38()
            }
            else if(n2==29|n2==32|n2==34|n2==36){
                e37()
                e38()
            }
        }
        else if(n1=='h'){
            if(n2<18)
            {
                h18()
                h28()
                h38()
            }
            else if(n2<27){
                h27()
                h28()
                h38()
            }
            else if(n2<35){
                h35()
                h38()
            }
        }
        else if(n1=='i'){
            if(n2<18)
            {
                i18()
                i28()
                i38()
            }
            else if(n2<27){
                i27()
                i28()
                i38()
            }
            else if(n2<35){
                i35()
                i38()
            }
        }




        
    });
    refreshdata()

}

function d17() {
    var total = 0
    for(var i=6;i<17;i++)
    {
        if ($('.input .d'+i).val()){
            total = parseFloat($('.input .d'+i).val()) + total
        }
        
    }
    $(".d17 span").text(total.toFixed(2))
}

function e17() {
    var total = 0
    for(var i=6;i<17;i++)
    {
        if ($('.input .e'+i).val()){
            total = parseFloat($('.input .e'+i).val()) + total
        }
        
    }
    $(".e17 span").text(total.toFixed(2))
}



function d26() {
    cal('d24,-d25,d26')
}
function e26() {
    cal('e24,-e25,e26')
}
function d28() {
    cal('d24,-d25,-d27,d28')
}
function e28() {
    cal('e24,-e25,-e27,e28')
}


function d37() {
    cal('d24,-d25,-d27,d29,d32,d34,d36,d37')
}

function e37() {
    cal('e24,-e25,-e27,e29,e32,e34,e36,e37')
}

function d38() {
    cal('d24,-d25,-d27,d29,d32,d34,d36,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d38')
}

function e38() {
    cal('e24,-e25,-e27,e29,e32,e34,e36,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e38')
}

function h18() {
    cal('h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18')
}
function i18() {
    cal('i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18')
}
function h27() {
    cal('h19,h20,h21,h22,h23,h24,h25,h26,h27')
}
function i27() {
    cal('i19,i20,i21,i22,i23,i24,i25,i26,i27')
}
function h28() {
    cal('h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h19,h20,h21,h22,h23,h24,h25,h26,h28')
}
function i28() {
    cal('i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i19,i20,i21,i22,i23,i24,i25,i26,i28')
}

function h35() {
    cal('h30,h31,h32,h33,h34,h35')
}
function i35() {
    cal('i30,i31,i32,i33,i34,i35')
}

function h38() {
    cal('h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h19,h20,h21,h22,h23,h24,h25,h26,h30,h31,h32,h33,h34,h38')
}
function i38() {
    cal('i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i19,i20,i21,i22,i23,i24,i25,i26,i30,i31,i32,i33,i34,i38')
}

function refreshdata() {
    d17()
    e17()
    d26()
    e26()
    d28()
    e28()
    d37()
    e37()
    d38()
    e38()
    h18()
    i18()
    h27()
    i27()
    h28()
    i28()
    h35()
    i35()
    h38()
    i38()
}


function cal(str) {
    var total = 0
    var lst_s = str.split(',')
    var res_s = lst_s[lst_s.length-1]
    lst_s = lst_s.slice(0,lst_s.length-1)
    for (var i=0;i<lst_s.length;i++){
        var s = lst_s[i]
        var sign = 1
        if (s[0] == '-'){
            sign = -1
            s = s.slice(1)
        }
        if ($('.input .'+s).val()){
            total = total + parseFloat($('.input .'+s).val()) * sign
        }
    }
    $("." + res_s + " span").text(total.toFixed(2))
}



var wb;//读取完成的数据
var rABS = false; //是否将文件读取为二进制字符串

function importf(obj) {//导入
    if(!obj.files) {
        return;
    }
    var f = obj.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
        var data = e.target.result;
        if(rABS) {
            wb = XLSX.read(btoa(fixdata(data)), {//手动转化
                type: 'base64'
            });
        } else {
            wb = XLSX.read(data, {
                type: 'binary'
            });
        }
        //wb.SheetNames[0]是获取Sheets中第一个Sheet的名字
        //wb.Sheets[Sheet名]获取第一个Sheet的数据
        deal_excel(wb)
    };
    if(rABS) {
        reader.readAsArrayBuffer(f);
    } else {
        reader.readAsBinaryString(f);
    }
}

function fixdata(data) { //文件流转BinaryString
    var o = "",
        l = 0,
        w = 10240;
    for(; l < data.byteLength / w; ++l) o += String.fromCharCode.apply(null, new Uint8Array(data.slice(l * w, l * w + w)));
    o += String.fromCharCode.apply(null, new Uint8Array(data.slice(l * w)));
    return o;
}

function deal_excel(wb) {
    var ce=XLSX.utils.sheet_to_formulae(wb.Sheets[wb.SheetNames[1]]);
    var dic = new Array();
    for (var i=0;i<ce.length;i++){
        var c = ce[i].split('=')
        if (c.length == 2){
            dic[c[0]] = c[1].toLowerCase() 
        }
        else{
            window.alert(i + '  '+ ce[i]);
        }
    }
    for (let item in $(".input input")){
        console.log($(item).attr('name'))
    }
    var input = $(".input input")
    for (var i=0;i<input.length;i++){
        _name = $(input[i]).attr('name').toUpperCase().replace(/^(\s|\xA0)+|(\s|\xA0)+$/g, '')
        $(input[i]).val(dic[_name])
    }
    refreshdata()
}