# Guide for Adding New Pipeline Notebooks

## Overview

This repository uses Jupyter notebooks for different stages of the eye-tracking data processing pipeline. Each notebook should be self-contained, well-documented, and follow the established patterns.

## Current Pipeline Structure

1. **`block_synchronization.ipynb`** - Synchronization pipeline
   - Handles eye video synchronization to Open Ephys timebase
   - Performs jitter correction
   - Removes LED blink artifacts
   - Creates final eye data dataframes

2. **`data_verification.ipynb`** (to be added) - Data verification pipeline
   - Will verify data quality and consistency
   - Check for missing data, outliers, etc.

3. **Future pipelines** - Analysis and figure generation

## Best Practices for Adding a New Pipeline Notebook

### 1. File Location and Naming

- Place notebooks in: `src/eye_tracking_system_tools/preprocessing/`
- Use descriptive, lowercase names with underscores: `data_verification.ipynb`
- Keep names consistent with the pipeline stage

### 2. Notebook Structure

Follow this structure for consistency:

```python
# Cell 1: Imports
from pathlib import Path
import numpy as np
import pandas as pd
from eye_tracking_system_tools.preprocessing import BlockSync, utility_functions as uf
# ... other imports

# Cell 2: Helper Functions (if needed)
# Define any utility functions specific to this pipeline

# Cell 3: Configuration
experiment_path = Path(r"D:\sample_data_for_eye_repo")
block_numbers = [15]
animal = 'PV_106'
# ... other configuration

# Cell 4: Block Instantiation
block_collection = uf.block_generator(...)
# ... setup blocks

# Cell 5+: Pipeline Steps
# Each major step in its own cell with clear comments
```

### 3. Import Guidelines

**DO:**
- Use absolute imports: `from eye_tracking_system_tools.preprocessing import BlockSync`
- Import utility functions: `from eye_tracking_system_tools.preprocessing import utility_functions as uf`
- Keep imports at the top in a dedicated cell

**DON'T:**
- Use relative imports in notebooks
- Import from `preprocessing` directly (use full package path)
- Mix imports throughout the notebook

### 4. Using Existing Data Structures

The synchronization pipeline creates these key data structures:

- `block.final_sync_df` - Synchronized dataframe with Arena_TTL, L_eye_frame, R_eye_frame, etc.
- `block.left_eye_data` - Final left eye dataframe (created by `create_eye_data()`)
- `block.right_eye_data` - Final right eye dataframe (created by `create_eye_data()`)
- `block.le_df` / `block.re_df` - Raw eye dataframes (before final processing)

**For data verification, you should:**
- Load existing data: `load_final_sync_df(block)` if needed
- Or use `block.left_eye_data` and `block.right_eye_data` directly
- Verify data quality, check for missing values, outliers, etc.

### 5. Working with Legacy Code

When migrating from legacy files:

1. **Start with a copy**: Create the new notebook and paste your legacy code
2. **Update imports first**: Change all imports to use the new package structure
3. **Replace deprecated patterns**:
   - Old: `from preprocessing import BlockSync`
   - New: `from eye_tracking_system_tools.preprocessing import BlockSync`
4. **Update function calls**: Use class methods instead of standalone functions where possible
5. **Remove unused code**: Clean up rotation-related code, old API calls, etc.
6. **Test incrementally**: Test each cell as you update it

### 6. Environment Compatibility

- **Python 3.10.19**: All code must work with this version
- **Bokeh 3.x**: Use modern API (`width`/`height`, `scatter()` instead of `circle()`)
- **NumPy 2.x**: Be aware of deprecations (use `bool` instead of `np.bool`)
- **Pandas 2.x**: Check for API changes if using older code

### 7. Code Organization

**Within a notebook:**
- Group related operations in the same cell
- Use markdown cells for section headers
- Add comments explaining non-obvious operations
- Keep cells focused on one task

**Between notebooks:**
- Each notebook should be runnable independently (after prerequisites)
- Document dependencies (e.g., "Run block_synchronization.ipynb first")
- Save intermediate results to `block.analysis_path` for sharing between notebooks

### 8. Error Handling

- Add validation checks for required data structures
- Use informative error messages
- Check for missing files/data before processing
- Handle edge cases (empty arrays, all-NaN columns, etc.)

### 9. Output and Export

- Save results to `block.analysis_path` directory
- Use descriptive filenames: `data_verification_report.csv`
- Include metadata (timestamp, block number, etc.) in filenames or file contents
- Document output format in comments

### 10. Testing

Before committing:
- Run the entire notebook from top to bottom
- Verify it works with your sample data
- Check that outputs are correct
- Ensure no deprecation warnings (fix them if they appear)

## Example: Adding data_verification.ipynb

Here's a template structure:

```python
# Cell 1: Imports
from pathlib import Path
import numpy as np
import pandas as pd
from eye_tracking_system_tools.preprocessing import BlockSync, utility_functions as uf

# Cell 2: Configuration
experiment_path = Path(r"D:\sample_data_for_eye_repo")
block_numbers = [15]
animal = 'PV_106'

# Cell 3: Load blocks and data
block_collection = uf.block_generator(...)
for block in block_collection:
    # Load existing data if needed
    # Or use block.left_eye_data / block.right_eye_data directly

# Cell 4: Verification functions
def verify_data_quality(block):
    """Verify data quality for a block"""
    # Your verification logic here
    pass

# Cell 5+: Run verification
for block in block_collection:
    verify_data_quality(block)
```

## Checklist for New Pipeline Notebook

- [ ] Notebook placed in correct directory
- [ ] Imports use full package paths (`eye_tracking_system_tools.preprocessing`)
- [ ] No deprecated API calls (Bokeh, NumPy, etc.)
- [ ] Code tested with Python 3.10.19
- [ ] Works with existing data structures from previous pipelines
- [ ] Saves outputs to `block.analysis_path`
- [ ] Includes clear documentation/comments
- [ ] No rotation-related code (unless specifically needed)
- [ ] Follows the established notebook structure
- [ ] Runs end-to-end without errors
