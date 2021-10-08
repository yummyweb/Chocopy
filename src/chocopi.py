from Cocoa import NSObject, NSApplication, NSApp, NSWindow, NSButton, NSMenu, NSTextField, NSRoundedBezelStyle, NSFont, NSMenuItem, NSAlert, NSColor, NSProgressIndicator, NSSlider, NSScrollView, NSColorPanel
from PyObjCTools import AppHelper

class Chocopy:
    def __init__(self, title, size, location=None, alpha=1, callback=None, titlebar_transparent=False, opaque=True):
        launch_callback = callback
        win = NSWindow.alloc()
        self.callbacks = {}
        choco_self = self
        self.panels = {}

        class AppDelegate(NSObject):
            def applicationDidFinishLaunching_(self, aNotification):
                if launch_callback:
                    launch_callback()
                else:
                    pass
            
            def onClick_(self, sender):
                if choco_self.callbacks["button"]:
                    choco_self.callbacks["button"][1]()
                else:
                    pass

            def onChange_(self, sender):
                if choco_self.callbacks["slider"]:
                    choco_self.callbacks["slider"][0]["cb"](choco_self.callbacks["slider"][0]["this"])
                else:
                    pass

            def onChangeCheckbox_(self, sender):
                if choco_self.callbacks["checkbox"]:
                    choco_self.callbacks["checkbox"][0]["cb"](choco_self.callbacks["checkbox"][0]["this"])
            
            def applicationShouldHandleReopen_hasVisibleWindows_(self, app, flag):
                win.makeKeyAndOrderFront_(None)
                return True

        self.title = title
        self.app = NSApplication.sharedApplication()

        delegate = AppDelegate.alloc().init()
        app = NSApp()
        app.setDelegate_(delegate)
        menu = NSMenu.alloc().init()
        item = NSMenuItem.alloc().init()
        menu.addItemWithTitle_action_keyEquivalent_("Quit", "terminate:", "q")
        item.setSubmenu_(menu)
        main_menu = NSMenu.alloc().init()
        main_menu.addItem_(item)
        self.app.setMainMenu_(main_menu)

        if location:
            frame = (location, size)
            win.initWithContentRect_styleMask_backing_defer_(frame, 15, 2, 0)
        else:
            frame = ((400.0, 300.0), size)
            win.initWithContentRect_styleMask_backing_defer_(frame, 15, 2, 0)
            win.center()

        win.setTitle_(self.title)
        win.setLevel_(3)
        win.setTitlebarAppearsTransparent_(titlebar_transparent)
        win.setAlphaValue_(alpha)
        win.setOpaque_(opaque)

        self.win = win
    
    def set_max_size(self, size):
        self.win.setMaxSize_(size)


    def button(self, text, location, size, content_id=None, onclick=None, *bezel_style):
        btn = NSButton.alloc().initWithFrame_((location, size))
        if content_id == None:
            self.win.contentView().addSubview_(btn)
        else:
            self.panels[content_id].contentView().addSubview_(btn)

        btn.setTitle_(text)
        btn.setTarget_(self.app.delegate())
        self.callbacks["button"] = []
        self.callbacks["button"].append(onclick)
        btn.setAction_("onClick:")
        
        if bezel_style:
            btn.setBezelStyle_(bezel_style[0])
        else:
            btn.setBezelStyle_(NSRoundedBezelStyle)


    def label(self, text, location, size, *font_size):
        textlabel = NSTextField.alloc().initWithFrame_((location, size))
        self.win.contentView().addSubview_(textlabel)
        textlabel.setStringValue_(text)
        textlabel.setEditable_(False)

        if font_size:
            textlabel.setFont_(NSFont.systemFontOfSize_(font_size[0]))
        else:
            textlabel.setFont_(NSFont.systemFontOfSize_(12))

        textlabel.setBordered_(False)
        textlabel.setDrawsBackground_(False)
        textlabel.setSelectable_(True)
    

    def textfield(self, placeholder, location, size, *font_size):
        field = NSTextField.alloc().initWithFrame_((location, size))
        self.win.contentView().addSubview_(field)
        field.setPlaceholderString_(placeholder)

        if font_size:
            field.setFont_(NSFont.systemFontOfSize_(font_size[0]))
        else:
            field.setFont_(NSFont.systemFontOfSize_(12))


    def checkbox(self, location, size, title, onchange=None):
        check_btn = NSButton.alloc().initWithFrame_((location, size))
        check_btn.setTitle_(title)
        check_btn.setTarget_(self.app.delegate())
        self.callbacks["checkbox"] = []
        self.callbacks["checkbox"].append({
            "cb": onchange,
            "this": {
                "title": check_btn.title(),
                "setTitle": check_btn.setTitle_,
                "checked": check_btn.state(),
                "changeChecked": check_btn.setNextState,
                "setChecked": check_btn.setState_
            }
        })
        check_btn.setAction_("onChangeCheckbox:")
        check_btn.setButtonType_(3)
        self.win.contentView().addSubview_(check_btn)

    def progress(self, location, size, val):
        indicator = NSProgressIndicator.alloc().initWithFrame_((location, size))
        indicator.setMaxValue_(100.00)
        indicator.setDoubleValue_(val)
        self.win.contentView().addSubview_(indicator)
    
    
    def slider(self, location, size, val, onchange=None):
        slide = NSSlider.alloc().initWithFrame_((location, size))
        slide.setMaxValue_(100.00)
        slide.setDoubleValue_(val)
        slide.setTarget_(self.app.delegate())
        self.callbacks["slider"] = []
        self.callbacks["slider"].append({
            "cb": onchange,
            "this": {
                "value": slide.doubleValue(),
                "setValue": slide.setDoubleValue_
            }
        })
        slide.setAction_("onChange:")
        self.win.contentView().addSubview_(slide)

    def alert(self, text):
        alert_modal = NSAlert.alloc().init()
        alert_modal.setMessageText_(text)
        alert_modal.runModal()
    

    def panel(self, location, size, identifier, border=None):
        scrollview = NSScrollView.alloc().initWithFrame_((location, size))
        if border == "etched":
            scrollview.setBorderType_(3)
        elif border == "normal":
            scrollview.setBorderType_(1)
        else:
            scrollview.setBorderType_(0)

        self.win.contentView().addSubview_(scrollview)
        self.panels[identifier] = scrollview
    

    def run(self):
        self.win.display()
        self.win.orderFrontRegardless()
        AppHelper.runEventLoop()
