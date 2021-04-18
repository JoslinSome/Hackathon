from kivy.lang.builder import Builder

CircleProgress = Builder.load_string("""
<Bar>:
""")
screenHelp = """
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
Screen:


    search:search
    fav:fav
    curriculum:curriculum
    MDBottomNavigation:
        id: panel
        panel_color: 1, 1, 1, 1
        MDBottomNavigationItem:
            name: 'search'
            id: search
            on_tab_release: app.tab_switchRecur()
            text: 'search'
            icon: 'magnify'
            
        
                
            MDRectangleFlatButton:
                id: searchBtn
                text: "Search"
                pos_hint:{"center_x":0.7,"center_y":0.8}
                on_release: 
                    app.search()

                
        MDBottomNavigationItem:
            name: 'track'
            text: 'Curriculum'
            on_tab_release: app.tab_switchTrack()
            id:curriculum
            icon: 'book-open-page-variant'
            

        MDBottomNavigationItem:
            id:save
            name: 'save'
            text: 'Save'
            icon: 'trophy'
           
        MDBottomNavigationItem:
            id:fav
            name: 'Favorites'
            text: 'Favorites'
            on_tab_release: app.tab_switchView()
            icon: 'star'
            
            MDRoundFlatIconButton:
                icon: "star"
                text: "Add to Favorites"
                text_color: 1, 1, 1, 1
                md_bg_color: .27, .18, .08, .75
                pos_hint:{"center_x":0.5,"center_y":0.8}
                size_hint_x: .7
                on_release: 
                    app.addlist()
            
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Demo App"

            id: toolbar
            left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
            right_action_items: [["help-circle-outline",lambda x: app.helpReccuring()]]
            size_hint_y: None
            elevation: 10

        NavigationLayout:
            id: layout
            ScreenManager:
                id:manage
                viewAll:
            MDNavigationDrawer:
                id: nav_drawer
                size_hint_x: None   

                width: 300

                BoxLayout:
                    orientation: "vertical"
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: "Theme"
                                on_release: app.ThemeChange()
                                IconLeftWidget:  
                                    icon:"format-color-text"
                    Widget:
                    Widget:
    ScreenManager:
        MenuScreen:

            Widget:
            NavigationLayout:
                id: layout
                ScreenManager:
                    id:manage
                    viewAll:
                MDNavigationDrawer:
                    id: nav_drawer2
                    size_hint_x: None    
                    width: 300
                    BoxLayout:
                        orientation: "vertical"
                        Image: 

                        Widget:
                        Widget:

        ProfileScreen:
            id: profile
        UploadScreen:

<MenuScreen>:
    name: 'menu'

<UploadScreen>:
    name: 'upload'

<ProfileScreen>:


"""
dialogBox = """
Content:
    id:Content
    name: name
    cost: cost
    orientation: "vertical"
    spacing: "1dp"
    size_hint_y: None
    height: "200dp"
    MDTextField:
        id: name 
        hint_text: "Item Name"
        helper_text: "Example: Netflix,Rent"
        helper_text_mode: "on_focus"
        pos_hint:{"center_x":0.5,"center_y":0.8}
    MDTextField:
        hint_text: "Item Cost"
        text: "$"
        id: cost
        helper_text: "Please enter a value"
        helper_text_mode: "on_error"
        halign: "auto"
        pos_hint:{"center_x":0.5,"center_y":0.8}
    MDFlatButton:
        text: "Date:"
        on_press: app.show_date_picker()
        text_color: app.theme_cls.primary_color
"""
occurrence = """
MDLabel:
    text: app.recurringday
"""

dialogBox1 = """
Content1:
    searchbar:searchbar
    pos_hint:{"center_x":0.5,"center_y":1.35}
    size_hint_x:0.5
    MDTextField:
        id: searchbar
        mode: "rectangle"
        hint_text: "Search a major"
"""
