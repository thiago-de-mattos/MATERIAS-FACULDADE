let selectedHero = null;
let selectedEnemy = null;


document.querySelectorAll('#heroGrid .character-card').forEach(card => {
    card.addEventListener('click', function() {
        document.querySelectorAll('#heroGrid .character-card').forEach(c => 
            c.classList.remove('selected')
        );
        this.classList.add('selected');
        selectedHero = this.dataset.class;
        checkSelection();
    });
});


document.querySelectorAll('#enemyGrid .character-card').forEach(card => {
    card.addEventListener('click', function() {
        document.querySelectorAll('#enemyGrid .character-card').forEach(c => 
            c.classList.remove('selected')
        );
        this.classList.add('selected');
        selectedEnemy = this.dataset.class;
        checkSelection();
    });
});


function checkSelection() {
    const btn = document.getElementById('startBattleBtn');
    if (selectedHero && selectedEnemy) {
        btn.disabled = false;
    } else {
        btn.disabled = true;
    }
}


document.getElementById('startBattleBtn').addEventListener('click', function() {
    let hero, enemy;

 
    switch(selectedHero) {
        case 'Knight': 
            hero = new Knight('Encrid'); 
            break;
        case 'Sorcerer': 
            hero = new Sorcerer('Mestre dos Magos'); 
            break;
        case 'Paladin': 
            hero = new Paladin('Arthur'); 
            break;
        case 'corrupt_Knight': 
            hero = new corrupt_Knight('Guts'); 
            break;
    }


    switch(selectedEnemy) {
        case 'LittleMonster': 
            enemy = new LittleMonster(); 
            break;
        case 'BigMonster': 
            enemy = new BigMonster(); 
            break;
    }


    document.getElementById('selectionScreen').style.display = 'none';
    document.getElementById('battleScreen').style.display = 'block';

    let log = new Log(document.querySelector(".log"));
    const stage = new Stage(
        hero,
        enemy,
        document.querySelector("#char"),
        document.querySelector("#monster"),
        log
    );
    
    stage.start();
});
