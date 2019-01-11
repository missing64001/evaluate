window.onload=function(){
    var input = $('#lookup_companyInfo')

    
    var i1 = input.next()
    var i2 = i1.next()
    var i3 = i2.next()
    i3.css({width:'206px'})
    var i4 = i3.next()
    var i5 = i4.next()
    var i6 = i5.next()
    var i7 = i6.next()
    var i8 = i7.next()


    input.remove()
    i1.remove()
    i5.remove()
    i6.remove()
    i7.remove()
    i8.remove()

    var help = $(".help-inline")
    help.html("仅显示序号，不影响使用")
}