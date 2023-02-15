# Copyright (c) 2022 NVIDIA CORPORATION.  All rights reserved.
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

from functools import partial
from typing import (
    Optional,
    Sequence,
)

import omni.graph.core as og
from omni.kit.property.usd.custom_layout_helper import (
    CustomLayoutFrame,
    CustomLayoutGroup,
    CustomLayoutProperty,
)
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry

from omni.warp.scripts.kernelnode import (
    MAX_DIMENSIONS,
    SUPPORTED_ATTR_TYPES,
)
from omni.warp.scripts.props.codefile import get_code_file_prop_builder
from omni.warp.scripts.props.codestr import get_code_str_prop_builder
from omni.warp.scripts.props.editattrs import get_edit_attrs_prop_builder

def find_prop(
    props: Sequence[UsdPropertyUiEntry],
    name: str,
) -> Optional[UsdPropertyUiEntry]:
    """Finds a prop by its name."""
    try:
        return next(p for p in props if p.prop_name == name)
    except StopIteration:
        return None

class CustomLayout:
    """Custom UI for the kernel node."""

    def __init__(self, compute_node_widget):
        self.enable = True
        self.compute_node_widget = compute_node_widget
        self.node_prim_path = self.compute_node_widget._payload[-1]
        self.node = og.Controller.node(self.node_prim_path)

        self.dim_count_attr = og.Controller.attribute(
            "inputs:dimCount",
            self.node,
        )
        self.code_provider_attr = og.Controller.attribute(
            "inputs:codeProvider",
            self.node,
        )

        self.node.register_on_connected_callback(
            self._handle_node_attr_connected
        )
        self.node.register_on_disconnected_callback(
            self._handle_node_attr_disconnected
        )
        self.dim_count_attr.register_value_changed_callback(
            self._handle_dim_count_value_changed
        )
        self.code_provider_attr.register_value_changed_callback(
            self._handle_code_provider_value_changed
        )

    def _handle_node_attr_connected(
        self,
        attr_from: og.Attribute,
        attr_to: og.Attribute,
    ) -> None:
        """Callback for a node attribute having been disconnected."""
        if attr_to.get_name() == "inputs:codeStr":
            # Redraw the UI to update the view/edit code button label.
            self.refresh()

    def _handle_node_attr_disconnected(
        self,
        attr_from: og.Attribute,
        attr_to: og.Attribute,
    ) -> None:
        """Callback for a node attribute having been disconnected."""
        if attr_to.get_name() == "inputs:codeStr":
            # Redraw the UI to update the view/edit code button label.
            self.refresh()

    def _handle_dim_count_value_changed(self, attr: og.Attribute) -> None:
        """Callback for the dimension count attribute value having changed."""
        # Redraw the UI to display a different set of attributes depending on
        # the dimension count value.
        self.refresh()

    def _handle_code_provider_value_changed(self, attr: og.Attribute) -> None:
        """Callback for the code provider attribute value having changed."""
        # Redraw the UI to display a different set of attributes depending on
        # the code provider value.
        self.refresh()

    def refresh(self) -> None:
        """Redraws the UI."""
        self.compute_node_widget.rebuild_window()

    def apply(self, props) -> Sequence[UsdPropertyUiEntry]:
        """Builds the UI."""
        frame = CustomLayoutFrame(hide_extra=True)

        with frame:
            with CustomLayoutGroup("Add and Remove Attributes"):
                CustomLayoutProperty(
                    None,
                    display_name=None,
                    build_fn=get_edit_attrs_prop_builder(
                        self,
                        SUPPORTED_ATTR_TYPES,
                    ),
                )

            with CustomLayoutGroup("Inputs"):
                prop = find_prop(props, "inputs:device")
                if prop is not None:
                    CustomLayoutProperty(
                        prop.prop_name,
                        display_name=prop.metadata["customData"]["uiName"],
                    )

                prop = find_prop(props, "inputs:dimCount")
                if prop is not None:
                    CustomLayoutProperty(
                        prop.prop_name,
                        display_name=prop.metadata["customData"]["uiName"],
                    )

                dim_count = min(
                    max(
                        og.Controller.get(self.dim_count_attr),
                        0,
                    ),
                    MAX_DIMENSIONS,
                )
                for i in range(dim_count):
                    prop = find_prop(props, "inputs:dim{}".format(i + 1))
                    if prop is not None:
                        CustomLayoutProperty(
                            prop.prop_name,
                            display_name=prop.metadata["customData"]["uiName"],
                        )

                prop = find_prop(props, "inputs:codeProvider")
                if prop is not None:
                    CustomLayoutProperty(
                        prop.prop_name,
                        display_name=prop.metadata["customData"]["uiName"],
                    )

                code_provider = og.Controller.get(self.code_provider_attr)
                if code_provider == "embedded":
                    prop = find_prop(props, "inputs:codeStr")
                    if prop is not None:
                        CustomLayoutProperty(
                            prop.prop_name,
                            display_name=prop.metadata["customData"]["uiName"],
                            build_fn=partial(
                                get_code_str_prop_builder(self),
                                prop,
                            ),
                        )
                elif code_provider == "file":
                    prop = find_prop(props, "inputs:codeFile")
                    if prop is not None:
                        CustomLayoutProperty(
                            prop.prop_name,
                            display_name=prop.metadata["customData"]["uiName"],
                            build_fn=partial(
                                get_code_file_prop_builder(self),
                                prop,
                            ),
                        )
                else:
                    raise RuntimeError(
                        "Unexpected code provider '{}'".format(code_provider)
                    )

        return frame.apply(props)
