function reject_company(_id) {
    var reason = prompt('请提交驳回原因\n确认后进行提交')
    if (reason){
        window.location.href="/admin/company/reject?id=" + _id + "&reason=" + reason
    }

}

function verify_company(_id) {
    window.location.href="/admin/company/verify?id=" + _id
}

$(function(){
    var cores = $('.controls')
    console.log(cores.length)
    for (var i=0;i<cores.length;i++){
        if ($(cores[i]).children().length == 4 | $(cores[i]).children().length == 5)
        {
            // $(cores[i]).append($($(cores[i]).children()[0]))
            $($(cores[i]).children()[0]).remove()
        }
    }
})