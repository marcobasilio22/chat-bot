<template>
    <div id="home" class="container">
        <div class="bar bar-icons">
            <a href="/chat" class="icon-link">
                <i class="fa-regular fa-comment custom-size"></i>
            </a>
            <a href="#ticket" class="icon-link">
                <i class="fa-solid fa-ticket custom-size"></i>
            </a>
            <a href="#network" class="icon-link">
                <i class="fa-solid fa-network-wired custom-size"></i>
            </a>
            <a href="#chart" class="icon-link">
                <i class="fa-solid fa-chart-simple custom-size"></i>
            </a>
            <a href="#users" class="icon-link">
                <i class="fa-solid fa-users custom-size"></i>
            </a>
            <div class="space"></div>
            <a href="#question" class="icon-link">
                <i class="fa-solid fa-question custom-size"></i>
            </a>
            <a href="#bell" class="icon-link">
                <i class="fa-regular fa-bell custom-size"></i>
            </a>
            <a href="#gear" class="icon-link">
                <i class="fa-solid fa-gear custom-size"></i>
            </a>
        </div>
        <div class="bar options">
            <h2 class="dashboard">DashBoards</h2>
            <a href="#" class="link-text">Visão Geral</a> <br />
            <a href="#" class="link-text">Relatorios</a>
        </div>
        <div class="board">
            <div class="board-top">
                <div class="board-path">caminho >></div> <br />
                <div class="board-dashboard">DashBoard</div><br />
                <div class="board-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos, possimus.
                </div><br />
            </div>
            <div class="board-down">
                <div class="board-line"></div>
            </div>
            <div class="status-patch-container">
                <div class="system-status">
                    <h2>Status Do Sistema</h2>
                    <!-- Add your content here -->
                </div>
                <div class="patch-updates">
                    <h2>Patch De Atualizações</h2>
                    <p>Versão 000 - {{ currentDateTime }}</p>
                    <ul>
                        <li>
                            <strong>Atualização X</strong>
                            <p> {{ statusMensage }}</p>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            currentDateTime: new Date().toLocaleString(),
            statusMensage: 'Aqui ficará um mini texto explicando a atualização em poucas palavras.'
        }
    }
}
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css');
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');

#home {
    display: flex;
    height: 100vh;
    margin: 0;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.container {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    height: 100%;
    width: 100%;
}

.bar {
    height: 100vh;
}

.bar-icons {
    background-color: #DCDCDC;
    width: 70px;
    display: flex;
    flex-direction: column;
}

.icon-link {
    display: block;
    text-decoration: none;
    color: inherit;
}

i {
    padding: 20px;
}

.space {
    flex-grow: 1;
}

.options {
    background-color: #DCDCDC;
    width: 250px;
}

.custom-size {
    font-size: 1.5rem;
}

.dashboard {
    padding: 20px;
    text-align: initial;
    font-family: "Roboto Condensed", sans-serif;
}

.link-text {
    text-align: left;
    padding-left: 20px;
    color: inherit;
    text-decoration: none;
    font-size: 1rem;
    display: block;
    margin-bottom: 0px;
}

.board {
    flex: 1;
    padding: 20px;
    background-color: #fff;
}

.board-top {
    text-align: left;
    margin-top: 10px;
    margin-left: 10px;
}

.board-down {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 20px;
}

.board-line {
    display: flex;
    width: 100%;
    height: 1px;
    background-color: rgb(223, 222, 222);
}

.status-patch-container {
    display: flex;
    justify-content: space-between;
    padding: 20px;
    background-color: #ffffff;
    margin: 20px 0;
}

.system-status,
.patch-updates {
    flex: 1;
    margin-right: 10px;
    padding: 20px;
    background-color: #eaeaea;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.system-status:last-child,
.patch-updates:last-child {
    margin-right: 0;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}
</style>