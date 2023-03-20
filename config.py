# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import temas

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.popup.toolkit import (PopupRelativeLayout, PopupImage, PopupText)

from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

# Modificaciones
# NOTA: Antes de ejecutar esta configuracion, ejecuta primero
# 1packages.sh o bien asegurate de tener los
# paquetes y aplicaciones listadas en el script

# Configurar antes de ejecutar el archivo .py
#============================================
#disp_red="enp0s3" # Cambiar el nombre del dispositivo de red
user="von" # Nombre de usuario del dispositivo
#============================================

# Colores
# Temas de colores disponibles: TokyoNight, ArchRed, ArchBlue, ArchCold,
# TokyoNight2
colores = temas.TokyoNight()

## barra superior
fuente_pred = "Ubuntu Mono Nerd Font"
tamanobarra = 30
tamano_fuente = 16
## grupo de escritorios
tamano_iconos=20

## Funciones
# Definimos las decoraciones qtile_extras
path_op = {
    1:'arrow_left',
    2:'arrow_right',
    3:'rounded_left', 
    4:'rounded_right', 
    5:'forward_slash',
    6:'back_slash',
    7:'zig_zag',
}

powerline = {
    "decorations":[
        PowerLineDecoration(
        path=path_op[4],
        )
    ]
}

### Funcion de separador
def funseparador(padd):
    return widget.Sep(
        linewidth=0,
        padding=padd, #10,
        #foreground=,
        background=colores['colorbarra'],
        **powerline,
    )

### Funciones para rectangulo
def pt_icono(icono, colorfg, colorbg):
    return widget.TextBox(
        text=icono,
        foreground=colorfg,
        background=colorbg,
        fontsize=tamano_fuente +3
    )

### Funcion de menu de apagado
def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="/home/"+user+"/.iconos/lock.png",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("dm-tool lock")
            }
        ),
        PopupImage(
            filename="/home/"+user+"/.iconos/reboot.png",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupImage(
            filename="/home/"+user+"/.iconos/shutdown.png",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.spawn("poweroff")
            }
        ),
        PopupText(
            text="Lock",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center",
	    foreground=colores["color_inactivo"],
	    fontsize=tamano_fuente,
        ),
        PopupText(
            text="Reboot",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center",
	    foreground=colores["color_inactivo"],
	    fontsize=tamano_fuente,
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center",
	    foreground=colores["color_inactivo"],
	    fontsie=tamano_fuente,
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=500,
        height=150,
        controls=controls,
        background=colores['colorfgg1'],
        initial_focus=None,
	opacity=0.5,
    )

    layout.show(centered=True)

#===========================



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # abrir menu rofi
    Key([mod], "m", lazy.spawn("bash /home/"+user+"/.config/rofi/launchers/type-3/launcher.sh"), desc="Abrir menu rofi"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Control de volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Control de microfono

    # Control de brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Captura de pantalla
    Key([mod, "control"], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s -f")),

    # Muestra menu flotante de apagado
    Key([mod, "shift"], "q", lazy.function(show_power_menu)),
]

__groups = {
    1: Group("", layout="tile"),
    2: Group("", matches=[Match(wm_class=["firefox"])]),
    3: Group("", layout="tile"),
    4: Group("󰨞", matches=[Match(wm_class=["code"])]),
    5: Group("", matches=[Match(wm_class=["pcmanfm"])]),
    6: Group(""),
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0] 

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=colores['colorfgg1'],
        border_normal=colores['colorbarra'],
        border_focus_stack=["#ffffff", "#ffffff"],
        border_width=2,
        margin=[4, 4, 4, 4],
        margin_on_single = 6,
    ),
    layout.Max(
        margin=6,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Floating(),
    # layout.Matrix(      
    #    #border_focus_stack=["#d75f5f", "#8f3d3d"], 
    #    border_width=1,
    #    margin=4,
    #),
    #layout.MonadTall(),
    layout.MonadWide(
        border_focus=colores["colorfgg1"],
        border_normal=colores["colorbarra"],
        border_width=1,
        margin=2,
    ),
    #layout.RatioTile(),
    layout.Tile(
        border_focus=colores["colorfgg1"],
        border_normal=colores["colorbarra"],
        expand=False,
        margin=4,
        shift_windows=True,
    ),
    layout.TreeTab(
        active_bg=colores['colorfgg1'],
        active_fg=colores['colorbarra'],
        bg_color=colores['colorbarra'],
        border_width=1,
        font=fuente_pred,
        fontsize=tamano_fuente,
        inactive_bg=colores['colorbarra'],
        inactive_fg=colores['colorfgg1'],
        margin_left=2,
        sections=['Workspace'],
        section_fontsize=tamano_fuente,
    ),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font=fuente_pred,
    fontsize=tamano_fuente,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background=colores['colorbgg4'],
                    **powerline,
                ),
                
                widget.GroupBox(
                    background=colores["colorbggv"],
                    #block_highlight_text_color="#f8713b",
                    active=colores['color_activo'],
                    border_width=1,
                    disable_drag=True,
                    fontsize=tamano_iconos,
                    highlight_method='block',
                    inactive=colores['color_inactivo'],
                    urgent_alert_method="block",
                    urgent_border="#F8713B",
                    this_current_screen_border=colores["colorseleccion"],
                    magin_x=-10,
                    margin_y=3,
                    padding_x=8,
                    padding_y=5,
                    **powerline,
                ),

                funseparador(10),

                #widget.Prompt(),
                widget.WindowName(
                    foreground=colores['colordetexto1'],
                ),

                #funseparador(10),
		        funseparador(10),

                # GRUPO 1
                #=========================================================== 
		        widget.Sep(
                    linewidth=0,
                    padding=20,
                    background=colores['colorfgg1'],
                    **powerline,
                ),
                #===========================================================
                
                # GRUPO 2
                #===========================================================
                pt_icono("", colores['colorfgg2'], colores['colorbgg2']),
                widget.Memory(
                    foreground = colores['colorfgg2'],
                    background = colores['colorbgg2'],
                    measure_mem='M',
                    format='{MemUsed: .0f}{mm}',
                ),

                pt_icono(" 󰚰", colores['colorfgg2'], colores['colorbgg2']),
                widget.CheckUpdates(
                    background=colores['colorbgg2'],
                    colour_have_updates=colores['color_actualizaciones'],
                    colour_no_updates=colores['colorfgg2'],
                    no_update_string="Up:0",
                    display_format="Up:{updates}",
                    update_interval=30,
                    distro="Arch_checkupdates",
                    **powerline,
                ),
                #===========================================================

                # GRUPO 3
                #===========================================================
                widget.Clock(
                    background=colores['colorbgg3'],
                    foreground=colores['colorfgg3'],
                    format="%Y-%m-%d %a %I:%M %p",
                    **powerline,
                ),
                #===========================================================

                # GRUPO 4
                #===========================================================
		        widget.Systray(
                    icon_size=tamano_iconos,
                ),

                widget.PulseVolume(
                    foreground=colores['colordetexto1'],
                    #background=colores['colorbgg3'],
                    limit_max_volume=True,
                    fontsize=tamano_fuente,
		            **powerline,
                ),

                widget.QuickExit(
                    default_text='[X]',
                    countdown_format='[{}]',
                    #foreground=colores['colorfgg4'],
                    background=colores['colorbgg4'],
                ),
                #===========================================================
            ],
            size = tamanobarra,
            background = colores['colorbarra'],
            opacity=0.9,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
       

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

auto = [
    #"bash /home/"+user+"/.screenlayout/resolucion.sh", # configuracion para ajustar la resolucion de VirtualMachine
    "nitrogen --random /home/"+user+"/Imagenes --set-zoom-fill &",
    "nm-applet &",
    "picom &",
    "cbatticon &",
    "volumeicon &",
]

for x in auto:
    os.system(x)
