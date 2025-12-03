说明：
该项目考试的题目顺序是随机的。建议使用脚本（法1）。
1.考试脚本可自动注入答案到题目下方；
2.复制按钮可一键复制所有题目和答案；

法1：tampermonkey 下粘贴js/下代码


法2：
F12 -- 开发者模式：
console控制台
粘贴代码：

``` javascript
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

```