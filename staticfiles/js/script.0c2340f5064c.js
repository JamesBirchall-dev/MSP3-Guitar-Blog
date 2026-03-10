// wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', function() {
    // ...existing code...
        // Summernote mobile/desktop initialization
        function isMobileDevice() {
            return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        }

        var summernoteSelector = document.querySelectorAll('.summernote');
        if (summernoteSelector.length > 0) {
            if (isMobileDevice()) {
                $(summernoteSelector).summernote({
                    airMode: true
                });
            } else {
                $(summernoteSelector).summernote({
                    toolbar: [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['insert', ['link', 'picture']]
                    ]
                });
            }
        }
});