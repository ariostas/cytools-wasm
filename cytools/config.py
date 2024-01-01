# =============================================================================
# This file is part of CYTools.
#
# CYTools is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# CYTools is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# CYTools. If not, see <https://www.gnu.org/licenses/>.
# =============================================================================
#
# -----------------------------------------------------------------------------
# Description:  This module contains various configuration variables for
#               experimental features and custom installations.
# -----------------------------------------------------------------------------

# 'standard' imports
import warnings
import os

# The number of CPU threads to use in some computations, such as finding the
# extremal rays of a cone. When set to None, then it uses all available threads.
n_threads = None

# Lock experimental features by default.
_exp_features_enabled = False

def enable_experimental_features():
    """
    **Description:**
    Enables the experimental features of CYTools. For more information read the
    [experimental features page](./experimental).

    **Arguments:**
    None.

    **Returns:**
    Nothing.

    **Example:**
    We enable the experimental features.
    ```python {2}
    import cytools
    cytools.config.enable_experimental_features()
    ```
    """
    global _exp_features_enabled
    _exp_features_enabled = True
    warnings.warn("\n**************************************************************\n"
                  "Warning: You have enabled experimental features of CYTools.\n"
                  "Some of these features may be broken or not fully tested,\n"
                  "and they may undergo significant changes in future versions.\n"
                  "**************************************************************\n")
