const viewer = pannellum.viewer('panorama', {
    "autoLoad": true,
    "showZoomCtrl": false,
    "showFullscreenCtrl": false,
    "preview": true,
    "default": {
        "firstScene": "circle",
        "sceneFadeDuration": 1000,
    },
    "scenes": {
        "circle": {
            "title": "Mason Circle",
            "hfov": 200,
            "pitch": 0,
            "yaw": 0,
            "type": "equirectangular",
            "panorama": "https://pannellum.org/images/alma.jpg",
            "hotSpots": []
        }
    }
});
const holdTrigger = $('.pnlm-dragfix');
let timeOutId = 0;

function mouseupListener(event) {
    const yaw = viewer.getYaw();
    const pitch = viewer.getPitch();
    const posPitch = viewer.mouseEventToCoords(event)[0];
    const posYaw = viewer.mouseEventToCoords(event)[1];
    const posX = event.offsetX;
    const posY = event.offsetY;
    alertify.prompt("Scene ID", function (e, str) {
        simulateMouseClick(document.querySelector('*'));
        if (e) {
            addHotSpot(posPitch, posYaw, str, str);
        }
        console.log(viewer.getConfig());
        console.log(viewer.getConfig().hotSpots)
    });
}

function simulateMouseClick(targetNode) {
    function triggerMouseEvent(targetNode, eventType) {
        const clickEvent = document.createEvent('MouseEvents');
        clickEvent.initEvent(eventType, true, true);
        targetNode.dispatchEvent(clickEvent);
    }

    ["mouseover", "mousedown", "mouseup", "click"].forEach(function (eventType) {
        triggerMouseEvent(targetNode, eventType);
    });
}

function addHotSpot(posPitch, posYaw, title, sceneId) {
    viewer.addHotSpot({
        "pitch": posPitch,
        "yaw": posYaw,
        "type": "scene",
        "text": title,
        "sceneId": `${sceneId}`
    }, 'circle')
}

holdTrigger.on('mousedown', function (e) {
    timeOutId = setTimeout(() => mouseupListener(e), 1000);
}).bind('mouseup mouseleave', () => {
    clearTimeout(timeOutId);
});