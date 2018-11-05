function submit_lock() {
    if (confirm('提交后数据不可更改\n请确认是否提交')){
        console.log(1)
        window.location.href="/admin/company/confirm"
    }

}