function verificarOutrosDefaults(checkbox) {
    const defaults = document.querySelectorAll('[id^="id_clienteendereco_set"][id$="-default"]');
    if (checkbox.checked) {
        defaults.forEach(function (item){
            if (item !== checkbox){
                item.checked = false;
            }
        })
    }
}