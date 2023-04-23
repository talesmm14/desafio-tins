function buscarEnderecoPorCep(id) {
    console.log('Chamou!' + document.getElementById('id_clienteendereco_set-' + id + '-cep').value);
    const buscar = document.querySelector("#id_clienteendereco_set-" + id + "-buscar");
    if (buscar != null) {
        const cep = document.getElementById('id_clienteendereco_set-' + id + '-cep').value.replace('-', '').replace('.', '');
        fetch('https://viacep.com.br/ws/' + cep + '/json/')
            .then(function (response) {
                console.log('entrou')
                return response.json();
            })
            .then(function (data) {
                if (!('erro' in data)) {
                    document.getElementById('id_clienteendereco_set-' + id + '-logradouro').value = data.logradouro;
                    document.getElementById('id_clienteendereco_set-' + id + '-bairro').value = data.bairro;
                    document.getElementById('id_clienteendereco_set-' + id + '-localidade').value = data.localidade;
                }
            })
            .catch(function (error) {
                console.log('Erro ao buscar dados do CEP: ' + error);
            });
    }
}