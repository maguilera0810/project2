document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#boton').disabled = true;

    document.querySelector('#msg').onkeyup = () => {
        if (document.querySelector('#msg').value.length > 0)
            document.querySelector('#boton').disabled = false;
        else
            document.querySelector('#boton').disabled = true;
    };

    document.querySelector('#volver').onclick = () => {
        localStorage.setItem('channel', 'home')
    }

    document.querySelector("#salir").onclick = () => {
        localStorage.clear()
    }
    console.log("conectado")
        // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure buttons
    socket.on('connect', () => {

        document.querySelector('#boton').onclick = () => {
            const mensaje = document.querySelector('#msg').value;
            document.getElementById("msg").value = ""
            document.querySelector('#boton').disabled = true;
            console.log(mensaje);
            console.log(channel);
            console.log("------------");
            console.log(localStorage);
            console.log("------------");

            socket.emit('send message', { 'mensaje': mensaje, 'channel': channel, 'color': localStorage.getItem("color"), 'username': localStorage.getItem('register'), 'date': new Date() });
        }
    });
    // When a new message is announced, add to the unordered list
    socket.on('new message', data => {
        console.log("//////////////////////")
        console.log(data)
        console.log("//////////////////////")
        if (data.channel === channel) {

            const tr = document.createElement('tr');

            if (data.username == localStorage.getItem('register')) {

                tr.innerHTML = `<td><div class="container"><div class="row justify-content-end"><div class="col-10"><div class="card"><div class="card-header" style="background-color:${data.color};">You</div><div class="card-body"><blockquote class="blockquote mb-0"><p>${data.mensaje}</p><footer class="blockquote-footer">${data.date} </footer></blockquote></div></div></div></div></div></td>`;
            } else {
                tr.innerHTML = `<td><div class="container"><div class="row justify-content-start"><div class="col-10"><div class="card"><div class="card-header" style="background-color:${data.color};">${data.username}</div><div class="card-body"><blockquote class="blockquote mb-0"><p>${data.mensaje}</p><footer class="blockquote-footer">${data.date} </footer></blockquote></div></div></div></div></div></td>`;

            }
            document.querySelector('#mensajes').append(tr);
            console.log("msg enviado")
            var count = document.getElementsByTagName('tr').length;
            if (count >= 100) {
                tester.removeChild(document.getElementById('mensajes').childNodes[0])
            }
        }
    });
});