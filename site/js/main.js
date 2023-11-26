let ul = document.querySelector('nav .ul');

function openMenu(){
    ul.classList.add('open');
}

function closeMenu(){
    ul.classList.remove('open');
}

//Validação de formulario

const campoNome = document.getElementById('formulario-nome')
const campoEmail = document.getElementById('formulario-email')
const campoAssunto = document.getElementById('formulario-assunto')
const campoMensagem = document.getElementById('formulario-textarea')
const botao = document.getElementById('formulario-botao')
const feedback = document.getElementById('feedback')


function limpaCampo(campo) {
    campo.value = ""
}

function limpaFeedback(classe) {
    feedback.innerHTML = ""
    feedback.classList.remove(classe)
}

function verificaCampo(valor) {
    return valor.trim().length > 2
}

function verificaEmail(valor) {
    if (!valor.includes('@')) {
        return false
    }
    const [ dominio, email ] = valor.split("@")
    if(!verificaCampo(dominio) || !verificaCampo(email)) {
        return false
    }
    return true
}

function formularioSubmetido(msg, classe) {
    const mensagem = document.createElement('p')
    mensagem.textContent = msg
    feedback.classList.add(classe)
    feedback.appendChild(mensagem)
    setTimeout(() => limpaFeedback(classe), 3000)
}

function sucesso() {
    limpaFeedback("erro")
    limpaCampo(campoNome)
    limpaCampo(campoEmail)
    limpaCampo(campoMensagem)
    limpaCampo(campoAssunto)
    formularioSubmetido("Formulario enviado com sucesso", "sucesso")
}

function erro() {
    limpaFeedback("sucesso")
    formularioSubmetido("Erro ao preencher um dos campos", "erro")
}

function onSubmit(event) {
    event.preventDefault()
    if (!verificaCampo(campoNome.value) || !verificaCampo(campoAssunto.value) || !verificaCampo(campoMensagem.value) || !verificaEmail(campoEmail.value)) {
        erro()
    } else {
        sucesso()
    }
}

//Evento de clique nos cards

function abrirModal(cardId){
    const card = document.querySelector(`#${cardId}`)

    const fade = card.querySelector(`#fade`)
    const modal = card.querySelector(`#modal`)
    fade.classList.remove('none')
    modal.classList.remove('none')
}

function pausarVideo(video) {
    const videoURL = video.src;
    video.src = videoURL;
}
function fecharModal(cardId) {
    const card = document.querySelector(`#${cardId}`)
    const fade = card.querySelector('#fade')
    const modal = card.querySelector('#modal')
    const videoIframe = card.querySelector('#video')
    fade.classList.add('none')
    modal.classList.add('none')

    pausarVideo(videoIframe)
}
const card = document.querySelector(`#${cardId}`)
