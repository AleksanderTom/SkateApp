$(document).ready(function () {

    var key = 'AIzaSyD0K7nk2vqvG4RyqFqDMadNpfwdEE2pBpM';
    var playlistId = 'PLmxvVi4Ors7aqc726ngHq1SwTrBGPjCSN';
    var URL = 'https://www.googleapis.com/youtube/v3/playlistItems';


    var options = {
        part: 'snippet',
        key: key,
        maxResults: 20,
        playlistId: playlistId
    };

    loadVids();

    function loadVids() {
        $.getJSON(URL, options, function (data) {
            var id = data.items[0].snippet.resourceId.videoId;
            mainVid(id);
            resultsLoop(data);
        });
    }

    function mainVid(id) {
        $('#video').html(`
					<iframe width="560" height="315" src="https://www.youtube.com/embed/${id}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
				`);
    }


    function resultsLoop(data) {

        $.each(data.items, function (i, item) {

            var thumb = item.snippet.thumbnails.medium.url;
            var title = item.snippet.title;
            var desc = item.snippet.description.substring(0, 100);
            var vid = item.snippet.resourceId.videoId;


            $('main').append(`
							<article class="item" data-key="${vid}">

								<img src="${thumb}" alt="" class="thumb">
								<div class="details">
									<h4>${title}</h4>
									<p>${desc}</p>
								</div>

							</article>
						`);
        });
    }

    // CLICK EVENT
    $('main').on('click', 'article', function () {
        var id = $(this).attr('data-key');
        mainVid(id);
    });


});

document.addEventListener("DOMContentLoaded", function () {

    var btnEasy = document.querySelector(".easy");
    var btnMedium = document.querySelector(".medium");
    var btnHard = document.querySelector(".hard");
    var trick = document.querySelector("#trick");
    var tutorialLink = document.querySelector("#tutorialLink");
    var Stance = document.querySelector(".Stance");
    var Obstacle = document.querySelector(".containerObstacle");
    var myGif = document.querySelector("#myImage");


    btnEasy.addEventListener('click', function () {
        var EASY_TRICKS = {
            'Kickflip': 'https://www.youtube.com/watch?v=-9ObaLwecNc',
            'Shove it': 'https://www.youtube.com/watch?v=W2btE3eLgX4',
            'Pop Shove it': 'https://www.youtube.com/watch?v=tyXwyN_t-is',
            'Heelflip': 'https://www.youtube.com/watch?v=phsJk5_jHkU',
            'Ollie': 'https://www.youtube.com/watch?v=QkeOAcj8Y5k',
            'Nollie': 'https://www.youtube.com/watch?v=8edqWNXp0WY&t=32s',
            'Halfcab': 'https://www.youtube.com/watch?v=P_BEJVUn7Jk',
            'Ollie North': 'https://www.youtube.com/watch?v=XQZluU6e6x4&t=59s',
            'Ollie South': 'https://www.youtube.com/watch?v=tjwe2N5lGwk',
        };

        var STANCE = {
            'regular': 'regular',
            'switch': 'switch',
            'fakie': 'fakie',
            'push mongo!': 'push mongo!',
            'nollie': 'nollie'
        };

        if (Stance.checked){
            // Random Key
            var stance = Object.keys(STANCE)[Math.floor(Math.random() * Object.keys(STANCE).length)];
            var easyTrick = Object.keys(EASY_TRICKS)[Math.floor(Math.random() * Object.keys(EASY_TRICKS).length)];

            trick.textContent = stance + ' ' + easyTrick;

            // Key Value
            tutorialLink.href = EASY_TRICKS[easyTrick];
        } else {
            // Random Key
            easyTrick = Object.keys(EASY_TRICKS)[Math.floor(Math.random() * Object.keys(EASY_TRICKS).length)];
            trick.textContent = easyTrick;

            // Key Value
            tutorialLink.href = EASY_TRICKS[easyTrick];
        }

    });

    btnMedium.addEventListener('click', function () {
        var MEDIUM_TRICKS = {
            'Bigspin': 'https://www.youtube.com/watch?v=MsPPeoeukoU&t=92s',
            'Backside Flip': 'https://www.youtube.com/watch?v=qgjU63ytvFw',
            'Varial Kickflip': 'https://www.youtube.com/watch?v=q0FxPQp2wHk',
            'Sex Change': 'https://www.youtube.com/watch?v=tV92ujeTOhE',
            'Frontside 180': 'https://www.youtube.com/watch?v=OqYb98vp0zI',
            'Backside 180': 'https://www.youtube.com/watch?v=5RtkYzx3TdE&t=267s',
            'Nose Grab': 'https://www.youtube.com/watch?v=sCGaZp2AOUM',
            'Indy Grab': 'https://www.youtube.com/watch?v=ACA24sQKLmc',
        };

        var STANCE = {
            'regular': 'regular',
            'switch': 'switch',
            'fakie': 'fakie',
            'push mongo!': 'push mongo!',
            'nollie': 'nollie'
        };

        if (Stance.checked){
            // Random Key
            var stance = Object.keys(STANCE)[Math.floor(Math.random() * Object.keys(STANCE).length)];
            var mediumTrick = Object.keys(MEDIUM_TRICKS)[Math.floor(Math.random() * Object.keys(MEDIUM_TRICKS).length)];
            trick.textContent = stance + ' ' + mediumTrick;

            // Key Value
            tutorialLink.href = MEDIUM_TRICKS[mediumTrick];
        } else {
            // Random Key
            mediumTrick = Object.keys(MEDIUM_TRICKS)[Math.floor(Math.random() * Object.keys(MEDIUM_TRICKS).length)];
            trick.textContent = mediumTrick;

            // Key Value
            tutorialLink.href = MEDIUM_TRICKS[mediumTrick];
        }

    });

    btnHard.addEventListener('click', function () {
        var HARD_TRICKS = {
            'Backside Heelflip': 'https://www.youtube.com/watch?v=BlGwoF8v3zo',
            'Big Heelflip': 'https://www.youtube.com/watch?v=Au2K85aCLYk',
            'Bigflip': 'https://www.youtube.com/watch?v=TuzfkgxbOeQ',
            'Biggerflip': 'https://www.youtube.com/watch?v=EOD2cEjqnvE',
            'Caballerial Flip': 'https://www.youtube.com/watch?v=89c5AcUEz88',
            '540 Flip': 'https://www.youtube.com/watch?v=9rcTOYJKwU8',
            'Fingerflip': 'https://www.youtube.com/watch?v=gcaE3VGl7qc',
            'Frontside Flip': 'https://www.youtube.com/watch?v=_YCXMS2_O6w',
            'Frontside Heelflip': 'https://www.youtube.com/watch?v=aN0jbylT3IY',
            'Front Foot Impossible': 'https://www.youtube.com/watch?v=U6sST0rO3mI',
            'Hardflip': 'https://www.youtube.com/watch?v=hZlSr6SQvds&t=245s',
            'Underflip': 'https://www.youtube.com/watch?v=2w6o-71a_u0',
            '360 Flip': 'https://www.youtube.com/watch?v=PnuobIzTPMs',
            'Laser Flip':'https://www.youtube.com/watch?v=B991k5v-cvE',
            'Hospital Flip': 'https://www.youtube.com/watch?v=aOxe8e0UTCs',
            'Impossible': 'https://www.youtube.com/watch?v=Wc500MYo6hg',
            'Inward Heelflip': 'https://www.youtube.com/watch?v=0SmsV8Xb7fA',
            'Kickback Flip': 'https://www.youtube.com/watch?v=hjxCVeDJcG0',
        };

        var STANCE = {
            'regular': 'regular',
            'switch': 'switch',
            'fakie': 'fakie',
            'push mongo!': 'push mongo!',
            'nollie': 'nollie'
        };

        if (Stance.checked){
            // Random Key
            var stance = Object.keys(STANCE)[Math.floor(Math.random() * Object.keys(STANCE).length)];
            var HardTrick = Object.keys(HARD_TRICKS)[Math.floor(Math.random() * Object.keys(HARD_TRICKS).length)];
            trick.textContent = stance + ' ' + HardTrick;

            // Key Value
            tutorialLink.href = HARD_TRICKS[HardTrick];
        } else {
            // Random Key
            HardTrick = Object.keys(HARD_TRICKS)[Math.floor(Math.random() * Object.keys(HARD_TRICKS).length)];
            trick.textContent = HardTrick;

            // Key Value
            tutorialLink.href = HARD_TRICKS[HardTrick];
        }

    });

});