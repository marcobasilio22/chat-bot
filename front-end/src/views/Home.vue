<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

    <div id="home" class="container">
        <div class="bar bar-icons">
            <a href="#comment" class="icon-link">
                <i class="fa-regular fa-comment custom-size"></i>
            </a>
            <a href="#ticket" class="icon-link">
                <i class="fa-solid fa-ticket custom-size"></i>
            </a>
            <a href="#network" class="icon-link">
                <i class="fa-sharp-duotone fa-solid fa-network-wired custom-size"></i>
            </a>
            <a href="#chart" class="icon-link">
                <i class="fa-solid fa-chart-simple custom-size"></i>
            </a>
            <a href="#users" class="icon-link">
                <i class="fa-solid fa-users custom-size"></i>
            </a>
            <div class="space">
            </div>
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
            <a href="#" class="link-text">Visão Geral</a> <br>
            <a href="#" class="link-text">Relatorios</a>
        </div>
        <div class="board">
            <!-- <div> caminho >></div> <br>
            <div> DashBoard</div><br>
            <div>lor</div><br> -->
        </div>
    </div>
</template>

<script>
export default {
    name: 'App'
}
</script>

<style>
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
    background-color: #DCDCDC	;
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
    background-color: #DCDCDC	;
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
    padding: 2000px;
    background-color: red;
}
</style>
