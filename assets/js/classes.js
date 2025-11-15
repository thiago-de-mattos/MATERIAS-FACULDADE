class Character {
    _life = 1;
    maxlife = 1;
    attack = 0;
    defense = 0;
    image = '';

    constructor(name, image = ''){
        this.name = name;
        this.image = image;
    }

    get life(){
        return this._life;
    }

    set life(newLife){
        this._life = newLife < 0 ? 0 : newLife;
    }
}

class corrupt_Knight extends Character {
    constructor(name){
        super(name, 'assets/img/guts.jpeg');
        this.life = 100;
        this.attack = 10;
        this.defense = 8;
        this.maxlife = this.life;
        this.deathAttempts = 0;
        this.isBerserk = false;
    }
}

class Berserk extends Character { 
    constructor(originalName){
        super(`${originalName} (BERSERK)`, 'assets/img/guts_Berserk.jpg'); // ← NOME DO ARQUIVO
        this.life = 80;
        this.attack = 18; 
        this.defense = 12;
        this.maxlife = this.life;
        this.isBerserk = true; 
    }
}

class Knight extends Character {
    constructor(name){
        super(name, 'assets/img/knight.jpg');
        this.life = 100;
        this.attack = 10;
        this.defense = 8;
        this.maxlife = this.life;
    }
}

class Sorcerer extends Character {
    constructor(name){
        super(name, 'assets/img/mestre_dos_magos.png');
        this.life = 80;
        this.attack = 15;
        this.defense = 3;
        this.maxlife = this.life;
    }
}

class Paladin extends Character {
    constructor(name){
        super(name, 'assets/img/Paladin.avif');
        this.life = 150;
        this.attack = 5;
        this.defense = 15;
        this.maxlife = this.life;
    }
}

class LittleMonster extends Character {
    constructor(){
        super('Little Monster', 'assets/img/esqueleto.jpEg');
        this.life = 40;
        this.attack = 4;
        this.defense = 4;
        this.maxlife = this.life;
    }
}

class BigMonster extends Character {
    constructor(){
        super('Big Monster', 'assets/img/rei lich.jpeg');
        this.life = 120;
        this.attack = 16;
        this.defense = 6;
        this.maxlife = this.life;
    }
}

class Stage {
    constructor(fighter1, fighter2, fighter1EL, fighter2EL, logObject){
        this.fighter1 = fighter1;
        this.fighter2 = fighter2;
        this.fighter1EL = fighter1EL;
        this.fighter2EL = fighter2EL;
        this.log = logObject;
        this.currentTurn = 1;
        this.fighter1Attacks = 0;
        this.fighter2Attacks = 0;
        this.originalFighter1 = fighter1;
    }

    start(){
        document.getElementById('heroImage').src = this.fighter1.image;
        document.getElementById('monsterImage').src = this.fighter2.image;
        
        this.update();
        this.log.addMessage(`🎮 A batalha nas sombras começa!`, 'system');
        this.log.addMessage(`--- Turno de ${this.fighter1.name} ---`, 'system');

        this.fighter1EL.querySelector('.attackbutton').addEventListener('click', () => {
            this.doAttack(this.fighter1, this.fighter2, 1);
        });

        this.fighter2EL.querySelector('.attackbutton').addEventListener('click', () => {
            this.doAttack(this.fighter2, this.fighter1, 2);
        });
    }

    getCurrentFighter(){
        return this.currentTurn === 1 ? this.fighter1 : this.fighter2;
    }

    getFighterType(fighter){
        if(fighter instanceof Knight || fighter instanceof Sorcerer || 
           fighter instanceof Paladin || fighter instanceof corrupt_Knight ||
           fighter instanceof Berserk){ // ← MUDADO
            return 'hero';
        } else {
            return 'monster';
        }
    }

    switchTurn(){
        this.currentTurn = this.currentTurn === 1 ? 2 : 1;
        this.fighter1Attacks = 0; 
        this.fighter2Attacks = 0;
        this.log.addMessage(`--- Turno de ${this.getCurrentFighter().name} ---`, 'system');
        this.update();
    }

    // ⚔️ Função para transformar em BERSERK
    transformToBerserk(fighter, attackerNumber){
        const originalName = fighter.name.replace(' (BERSERK)', '');
        const berserk = new Berserk(originalName); 
        
        if(attackerNumber === 1){
            this.fighter1 = berserk;
        } else {
            this.fighter2 = berserk;
        }

        // Atualiza a imagem
        if(attackerNumber === 1){
            document.getElementById('heroImage').src = berserk.image;
            this.fighter1EL.classList.add('berserk-active'); 
        } else {
            document.getElementById('monsterImage').src = berserk.image;
            this.fighter2EL.classList.add('berserk-active'); 
        }
        
        this.log.addMessage(`💀 ${originalName} VENDEU SUA ALMA À MARCA!`, 'dark');
        this.log.addMessage(`⚔️ ${berserk.name} RENASCE COMO GUERREIRO AMALDIÇOADO!`, 'dark');
        this.log.addMessage(`🗡️ A MARCA DO SACRIFÍCIO PULSA COM PODER BRUTAL!`, 'dark');
        this.log.addMessage(`⚡ Stats aumentados: ATK ${berserk.attack} | DEF ${berserk.defense}`, 'system');
        
        this.update();
        this.switchTurn();
    }

    doAttack(attacking, attacked, attackerNumber){
        // HABILIDADE ESPECIAL: Corrupt Knight vira BERSERK
        if (attacking.life <= 0 && attacking instanceof corrupt_Knight && !attacking.isBerserk){ // ← MUDADO
            attacking.deathAttempts++;
            
            this.log.addMessage(
                `💀 ${attacking.name} tenta atacar mesmo morto! (${attacking.deathAttempts}/3)`, 
                'dark'
            );

            if(attacking.deathAttempts >= 3){
                this.showDarkOffer(attacking, attackerNumber);
            }
            return;
        }

        if (attacking.life <= 0){
            alert('Você está morto!');
            return;
        }
        if(attacked.life <= 0){
            alert('Você está atacando um morto');
            return;
        }

        if(this.currentTurn !== attackerNumber){
            alert('Não é seu turno!');
            return;
        }
        if(attackerNumber === 1 && this.fighter1Attacks >= 1){
            alert('Você já atacou neste turno!');
            return;
        }
        if(attackerNumber === 2 && this.fighter2Attacks >= 1){
            alert('Você já atacou neste turno!');
            return;
        }

        let attackFactor = Math.random() * 2;
        let defenseFactor = Math.random() * 2;

        let actualAttack = attacking.attack * attackFactor;
        let actualDefense = attacked.defense * defenseFactor;

        let attackerType = this.getFighterType(attacking);
        let defenderType = this.getFighterType(attacked);

        if(actualAttack > actualDefense){
            let damage = actualAttack - actualDefense;
            attacked.life -= damage;
            
            let attackIcon = attacking.isBerserk ? '🗡️' : '⚔️'; 
            
            this.log.addMessage(
                `${attackIcon} ${attacking.name} causou ${damage.toFixed(2)} de dano em ${attacked.name}`,
                attackerType
            );

            if(attacked.life <= 0){
                this.log.addMessage(`💀 ${attacked.name} foi derrotado!`, defenderType);
                this.log.addMessage(`🏆 ${attacking.name} venceu a batalha!`, 'system');
            }

            if(damage < 1){
                this.log.addMessage(
                    `⚡ Ataque muito fraco! ${attacking.name} ganha mais um turno!`,
                    'system'
                );
            } else {
                if(attackerNumber === 1){
                    this.fighter1Attacks++;
                } else {
                    this.fighter2Attacks++;
                }
                this.switchTurn();
            }
        } else {      
            let lifeRecovery = Math.min(10, Math.max(2, actualDefense * 0.05));
            
            let oldLife = attacked.life;
            attacked.life = Math.min(attacked.maxlife, attacked.life + lifeRecovery);
            let actualRecovery = attacked.life - oldLife;
            
            this.log.addMessage(
                `🛡️ ${attacked.name} defendeu o ataque de ${attacking.name}`,
                defenderType
            );
            
            if(actualRecovery > 0){
                this.log.addMessage(
                    `💚 ${attacked.name} recuperou ${actualRecovery.toFixed(2)} de vida!`,
                    defenderType
                );
            }

            if(attackerNumber === 1){
                this.fighter1Attacks++;
            } else {
                this.fighter2Attacks++;
            }
            this.switchTurn();
        }

        this.update();
    }

    showDarkOffer(fighter, attackerNumber){
        const modal = document.getElementById('darkModal');
        const darkName = document.getElementById('darkName');
        
        darkName.textContent = fighter.name;
        modal.style.display = 'block';

        document.getElementById('acceptDeal').onclick = () => {
            modal.style.display = 'none';
            this.transformToBerserk(fighter, attackerNumber); 
        };

        document.getElementById('refuseDeal').onclick = () => {
            modal.style.display = 'none';
            this.log.addMessage(
                `${fighter.name} recusou a Marca do Sacrifício. Sua humanidade permanece intacta.`,
                'system'
            );
            this.log.addMessage(
                `💀 ${fighter.name} aceitou o destino final...`,
                'dark'
            );
        };
    }

    update(){
        this.fighter1EL.querySelector(".name").innerHTML =
            `${this.fighter1.name} - ${this.fighter1.life.toFixed(1)}/${this.fighter1.maxlife} HP`;
        let f1pct = (this.fighter1.life / this.fighter1.maxlife) * 100;
        this.fighter1EL.querySelector(".bar").style.width = `${f1pct}%`;

        this.fighter2EL.querySelector(".name").innerHTML =
            `${this.fighter2.name} - ${this.fighter2.life.toFixed(1)}/${this.fighter2.maxlife} HP`;
        let f2pct = (this.fighter2.life / this.fighter2.maxlife) * 100;
        this.fighter2EL.querySelector(".bar").style.width = `${f2pct}%`;

        if(this.currentTurn === 1){
            this.fighter1EL.style.opacity = '1';
            this.fighter2EL.style.opacity = '0.5';
            this.fighter1EL.classList.add('active');
            this.fighter2EL.classList.remove('active');
        } else {
            this.fighter1EL.style.opacity = '0.5';
            this.fighter2EL.style.opacity = '1';
            this.fighter1EL.classList.remove('active');
            this.fighter2EL.classList.add('active');
        }
    }
}

class Log {
    list = [];

    constructor(listEL){
        this.listEL = listEL;
    }

    addMessage(msg, type = 'system'){
        this.list.push({ message: msg, type: type });
        this.render();
    }

    render(){
        this.listEL.innerHTML = '';
        this.list.slice(-20).reverse().forEach(item => {
            this.listEL.innerHTML += `<li class="log-${item.type}">${item.message}</li>`;
        });
    }
}