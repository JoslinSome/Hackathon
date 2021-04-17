from kivy.lang.builder import Builder

CircleProgress = Builder.load_string("""
<Bar>:
""")
screenHelp = """
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
Screen:


    search:search
    MDBottomNavigation:
        id: panel
        panel_color: 1, 1, 1, 1
        MDBottomNavigationItem:
            name: 'search'
            id: search
            on_tab_release: app.tab_switchRecur()
            text: 'search'
            icon: 'magnify'
            
            MDTextField:
                id: searchbar
                mode: "rectangle"
                pos_hint:{"center_x":0.5,"center_y":0.8}
                size_hint_x:0.5
                hint_text: "Search a major"
                
            MDRectangleFlatButton:
                id: searchBtn
                text: "Search"
                pos_hint:{"center_x":0.7,"center_y":0.7}
                on_release: 
                    app.search()

                
        MDBottomNavigationItem:
            name: 'track'
            text: 'Curriculum'
            on_tab_release: app.tab_switchTrack()
            id:track
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
<Content1>:
    id: Content1
    orientation: "vertical"
    size_hint_y: None
    height: "200dp"
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Item Name: "+  app.tempName
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
        MDLabel:
            text: "Item Cost: "+  app.tempCost
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
        MDLabel:
            text: "Occurs Monthly on the "+ app.recurringday
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color

<help>:
    MDLabel:
        text: "Track your recurring monthly payments like Rent and Netflix. Click on the plus icon at the bottom left of the screen to add a recurring item!"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<helpTrack>:
    MDLabel:
        text: "Keep track of the money you gain and spend, press the buttons below to create an Item"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<helpOverview>:
    MDLabel:
        text: "View your monthly spendings so far. First create a spending item on the reccuring or track tab before being able to view"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<helpSave>:
    MDLabel:
        text: "Want to save up for something?, create a new item and keep track of how much hou have saved"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<Existing>:
    MDLabel:
        text: "The Item you entered already exists. Please change its Name" 
<Content2>:
    title: "hello" 
    name: name
    cost: cost
    BoxLayout:
        spacing: "20dp"
        MDTextField: 
            id: name
            hint_text: "Item Name:"
        MDTextField:
            hint_text: "Item Cost:"
            id:cost
            text: "$"

<Content3>:
    month:month
    MDTextField:
        id: month
        hint_text: "Amount"
        text: "$"

<Content4>:
    title: "hello" 
    name: name
    cost: cost
    BoxLayout:
        spacing: "20dp"
        MDTextField: 
            id: name
            hint_text: "Item Name:"
        MDTextField:
            hint_text: "Item Cost:"
            id:cost
            text: "$"
<Content5>:
    title: "hello" 
    MDLabel:
        text: "The Item you entered already exists, would you like to add onto it? "
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.6}

<Warning>:
    MDLabel:
        text: "Are you sure you want to delete this item? "
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.6}
<Warning1>:
    MDLabel:
        text: "Are you sure you want to delete this item? "
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.6}
<Add>:
    title: "hello" 
    cost: cost
    BoxLayout:
        spacing: "20dp"
        MDTextField:
            hint_text: "Add amount:"
            id:cost
            text: "$"

"""
dialogBox2 = """
Content2:
    scroll: scroll
"""
viewScreen = """
<viewAll>:
    ScrollView:
"""

pannel = """
"""