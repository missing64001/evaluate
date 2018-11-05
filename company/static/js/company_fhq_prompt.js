function reject_company(_id) {
    var reason = prompt('请提交驳回原因\n确认后进行提交')
    if (reason){
        window.location.href="/admin/company/reject?id=" + _id + "&reason=" + reason
    }

}