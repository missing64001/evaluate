

$(function () {
    function _remove(as) {
        for (var i=0;i<as.length;i++){
            var ac = $($(as[i]).find('.readonly')[0])
            if (ac.text() == '-'){
                $(as[i]).parent().remove()
            }
            console.log(ac.text())
        }
    }
    var as = $('.field-xxtemp1 .field-xxtemp1')
    _remove(as)

    var as = $('.field-xxtemp2 .field-xxtemp2')
    _remove(as)

    var as = $('.field-xxtemp3 .field-xxtemp3')
    _remove(as)

    var as = $('.field-xxtempgz1 .field-xxtempgz1')
    _remove(as)

    var as = $('.field-xxtempgz2 .field-xxtempgz2')
    _remove(as)

    var as = $('.field-xxtempgz3 .field-xxtempgz3')
    _remove(as)

})

