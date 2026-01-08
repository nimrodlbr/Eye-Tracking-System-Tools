# Git Commit Instructions

## Summary of Changes

This commit includes the migration and cleanup of the eye-tracking preprocessing pipeline:

### Key Changes:
1. **Python 3.10.19 Compatibility**
   - Updated `environment.yml`, `pyproject.toml`, and `requirements.txt` for Python 3.10.19
   - Fixed `numpy` and `scipy` version constraints for compatibility
   - Added `StrEnum` compatibility shim for Python 3.10

2. **Import Fixes**
   - Fixed relative imports in `BlockSync_class.py` and `utility_functions.py`
   - Updated notebook imports to use `eye_tracking_system_tools.preprocessing`
   - Fixed `LsqEllipse` import to use `lsq-ellipse` package correctly

3. **Bokeh API Updates**
   - Replaced deprecated `plot_width`/`plot_height` with `width`/`height`
   - Fixed `range()` serialization issues (changed to `np.arange()`)
   - Replaced deprecated `fig.circle()` with `fig.scatter()`
   - Fixed static method calls (`self.bokeh_plotter` → `BlockSync.bokeh_plotter`)

4. **Pipeline Cleanup**
   - Removed standalone `create_eye_data` function from notebook
   - Updated to use class method `block.create_eye_data()`
   - Removed rotation matrix export (no longer used)
   - Updated export function to only save CSV files

5. **Bug Fixes**
   - Fixed empty peak array handling in `collect_lights_out_events`
   - Fixed boundary checking for peak expansion
   - Added data validation for NaN/Inf values

## Git Commands to Run

```bash
# 1. Check current status
git status

# 2. Create a new branch for this work (DO NOT commit to master)
git checkout -b preprocessing-pipeline-migration

# 3. Stage all changes
git add .

# 4. Create a commit with descriptive message
git commit -m "Migrate preprocessing pipeline to Python 3.10 and clean up rotation code

- Updated environment and dependencies for Python 3.10.19 compatibility
- Fixed all Bokeh API deprecations (plot_width/height, circle->scatter, range serialization)
- Fixed LsqEllipse import to use lsq-ellipse package correctly
- Removed rotation matrix functionality (no longer used)
- Updated notebook to use class method create_eye_data() instead of standalone function
- Fixed various bugs in collect_lights_out_events and bokeh_plotter
- Synchronization pipeline now fully functional on Python 3.10"

# 5. Push the branch to remote (if you have a remote configured)
git push -u origin preprocessing-pipeline-migration

# 6. Verify the commit
git log --oneline -1
```

## Important Notes

- **DO NOT** push to `master` branch - this is a work-in-progress
- The branch name `preprocessing-pipeline-migration` can be changed if you prefer
- After you add the data verification pipeline, you can merge this branch or continue on it
- Only merge to master when the full preprocessing stage is complete and tested
