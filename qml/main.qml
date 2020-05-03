import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    id: main_
    visible: true
    width: 800; height: 600

    function make_str(str) {
        return '<h1><font color="blue">' + str + '</font></h1>'
    }

    ColumnLayout {
        anchors.fill: parent
        Label {
            id: label_
            Layout.fillWidth: true
            Layout.fillHeight: true
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            text: make_str('I am a sample.')
        }
        Button {
            id: button_
            Layout.fillWidth: true
            Layout.maximumHeight: 50
            text: 'Click me!'
            onClicked: {
                label_.text = make_str('Hello world!')
            }
        }
    }
}
