// ==UserScript==
// @name        强制视频播放速度 16x - NCME
// @namespace   http://tampermonkey.net/
// @version     0.1
// @description 针对 ncme.org.cn 优化
// @author      luoyulong
// @match       https://www.ncme.org.cn/player/*
// @grant       none
// @run-at      document-start
// ==/UserScript==
(function() {
    const TARGET_RATE = 16;
    const INTERVAL_MS = 100;

    function enforcePlaybackRate() {

        const videos = document.querySelectorAll('video');

        if (videos.length === 0) {

            return;
        }

        videos.forEach(video => {

            if (video.playbackRate !== TARGET_RATE) {
                video.playbackRate = TARGET_RATE;

            }
        });
    }


    const intervalId = setInterval(enforcePlaybackRate, INTERVAL_MS);


})();
