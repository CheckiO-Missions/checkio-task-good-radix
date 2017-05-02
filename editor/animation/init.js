requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            functions: {
                js: 'goodRadix',
                python: 'checkio'
            }
        });
        io.start();
    }
);
