function getMediaPath() {
    return window.MEDIA_PREFIX;
}

// static images
function getStaticPath() {
    return window.STATIC_PREFIX;
}

export default {
    methods: {
        // uploaded images
        getUploadedImagePath: (path) => {
            return `${getMediaPath()}${path}`;
        },

        getStaticImagePath: (path) => {
            return `${getStaticPath()}${path}`;
        },
    }
}