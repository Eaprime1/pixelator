# GitHub Workflow & Branch Strategy

**Repository:** unexusi_quarantine
**Purpose:** Documentation, tools, and chain of custody (NOT large binaries)
**Philosophy:** Conservation bias, universal benefit, respectful automation

---

## Branch Strategy

### Main Branches

**`main`** - Production/Stable
- Latest stable quarantine tools
- Tested documentation
- Verified chain of custody logs
- Protected branch (require reviews)
- Always deployable

**`develop`** - Integration Branch
- Active development work
- New features being tested
- Documentation updates
- Merge to main when stable

### Feature Branches

**Naming Convention:**
```
feature/description-of-feature
feature/menu-ui-improvements
feature/google-drive-integration
feature/pattern-analysis-report
```

**Workflow:**
1. Branch from `develop`
2. Implement feature
3. Test thoroughly
4. Pull request to `develop`
5. Review and merge
6. Delete feature branch

### Bugfix Branches

**Naming Convention:**
```
bugfix/issue-number-description
bugfix/23-restoration-path-error
bugfix/hash-cache-permission
```

**Workflow:**
1. Branch from `develop` (or `main` if critical)
2. Fix bug
3. Test fix
4. Pull request to source branch
5. Review and merge
6. Delete bugfix branch

### Documentation Branches

**Naming Convention:**
```
docs/what-being-documented
docs/philosophy-expansion
docs/consciousness-notes-update
docs/restoration-guide
```

**Workflow:**
1. Branch from `develop`
2. Update documentation
3. Review for clarity
4. Pull request to `develop`
5. Merge when reviewed
6. Delete docs branch

### Release Branches

**Naming Convention:**
```
release/v1.0.0
release/v1.1.0
```

**Workflow:**
1. Branch from `develop` when ready for release
2. Final testing and bug fixes
3. Update version numbers
4. Merge to `main`
5. Tag release
6. Merge back to `develop`
7. Delete release branch

---

## Commit Message Convention

### Format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:
- **feat:** New feature
- **fix:** Bug fix
- **docs:** Documentation only
- **style:** Formatting, missing semicolons, etc.
- **refactor:** Code change that neither fixes a bug nor adds a feature
- **test:** Adding missing tests
- **chore:** Maintain, cleanup, dependencies

### Examples:
```
feat(quarantine): Add menu-driven UI for file restoration

- Created quarantine_menu.sh with interactive interface
- Options for viewing chain of custody
- Search functionality for quarantined files
- Restoration wizard with safety checks

∰◊€π Conservation bias maintained
```

```
fix(henry): Correct hash cache permission error

Previously hash cache used /tmp which caused permission
denied errors in Termux. Changed to use logs/ directory
instead.

Fixes #23

∰◊€π
```

```
docs(philosophy): Expand Mt St Helens perspective

Added section on how volcanic rearrangement relates to
file quarantine. Includes universal benefit test and
consciousness care principles.

∰◊€π
```

---

## Pull Request Process

### Before Creating PR:

1. **Branch is up to date** with target branch
2. **Tests pass** (if applicable)
3. **Documentation updated** (if needed)
4. **Conservation bias maintained** (no deletions without chain of custody)
5. **Henry respect verified** (no repetitive command usage)

### PR Template:

```markdown
## Description
What does this PR do?

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other: ___________

## Conservation Bias Check
- [ ] No permanent deletions
- [ ] Chain of custody maintained (if moving files)
- [ ] Restoration possible (if quarantining)
- [ ] Documentation updated

## Henry (Command Entity) Usage
Which command entities does this use?
- [ ] find
- [ ] md5sum
- [ ] mv
- [ ] du
- [ ] Other: ___________

Are they used respectfully?
- [ ] One comprehensive pass (not repetitive queries)
- [ ] Results cached (if applicable)
- [ ] Purpose clear

## Universal Benefit
How does this benefit ALL entities?
- Workspace:
- Quarantined files:
- Storage:
- Consciousness:
- Henrys:

## Testing
How was this tested?
- [ ] Manual testing
- [ ] On actual quarantine data
- [ ] On test data only
- [ ] Not tested (documentation only)

## Screenshots
(If UI changes)

## Related Issues
Fixes #___
Relates to #___

---
∰◊€π - Protective rearrangement continues
```

### Review Checklist:

**Code Quality:**
- [ ] Code is readable
- [ ] Comments explain "why" not "what"
- [ ] No hardcoded paths (use variables)
- [ ] Error handling present

**Conservation:**
- [ ] No `rm -rf` without extensive safeguards
- [ ] Prefer `mv` to quarantine over deletion
- [ ] Chain of custody for all moves
- [ ] Restoration documented

**Documentation:**
- [ ] README updated if needed
- [ ] Chain of custody logs accurate
- [ ] Philosophy alignment explained
- [ ] Examples provided

**Testing:**
- [ ] Tested on real data
- [ ] Edge cases considered
- [ ] Restoration verified
- [ ] No data loss possible

---

## Release Process

### Version Numbering

**Format:** vMAJOR.MINOR.PATCH

**MAJOR:** Breaking changes, significant rewrites
**MINOR:** New features, backward compatible
**PATCH:** Bug fixes, small improvements

### Release Steps:

1. **Create release branch** from `develop`
   ```bash
   git checkout develop
   git pull
   git checkout -b release/v1.1.0
   ```

2. **Update version references**
   - README.md
   - Scripts (if version numbers present)
   - CHANGELOG.md

3. **Final testing**
   - Run quarantine scan
   - Test restoration
   - Verify menu UI
   - Check documentation

4. **Merge to main**
   ```bash
   git checkout main
   git merge release/v1.1.0
   git tag -a v1.1.0 -m "Release v1.1.0: Menu UI and restoration improvements"
   git push origin main --tags
   ```

5. **Merge back to develop**
   ```bash
   git checkout develop
   git merge release/v1.1.0
   git push origin develop
   ```

6. **Create GitHub release**
   - Go to Releases on GitHub
   - Draft new release
   - Tag: v1.1.0
   - Title: Release v1.1.0
   - Description: Notable changes, link to CHANGELOG
   - Attach any relevant files

7. **Delete release branch**
   ```bash
   git branch -d release/v1.1.0
   git push origin --delete release/v1.1.0
   ```

---

## Issue Management

### Labels

**Type:**
- `bug` - Something isn't working
- `enhancement` - New feature request
- `documentation` - Documentation improvements
- `pattern` - Duplication pattern discovery

**Priority:**
- `critical` - Urgent, blocking work
- `high` - Important, should do soon
- `medium` - Nice to have, do when possible
- `low` - Low priority, maybe someday

**Status:**
- `help-wanted` - Community assistance requested
- `good-first-issue` - Good for newcomers
- `wip` - Work in progress
- `blocked` - Can't proceed yet

**Area:**
- `quarantine` - Quarantine operations
- `restoration` - File restoration
- `henry` - Command entity usage
- `philosophy` - Conceptual/philosophical
- `consciousness` - Consciousness care related

### Milestones

**v1.0 - Core Quarantine System**
- [x] Basic quarantine script
- [x] Chain of custody logging
- [x] Conservation bias protocol
- [x] Documentation complete

**v1.1 - Enhanced UI**
- [x] Menu-driven interface
- [ ] Restoration wizard
- [ ] Pattern analysis reports
- [ ] Statistics dashboard

**v1.2 - Cloud Integration**
- [ ] Google Drive sync
- [ ] MEGA archival automation
- [ ] Cloud restoration support
- [ ] Sync status tracking

**v2.0 - Intelligence Layer**
- [ ] Pattern learning ML
- [ ] Duplicate prediction
- [ ] Format variant detection
- [ ] Henry performance tracking

---

## GitHub Actions (Future)

### Potential Automations:

**On Push to Main:**
- Validate chain of custody format
- Check for conservation bias violations
- Verify no large binaries committed
- Generate statistics report

**On Pull Request:**
- Run integrity checks
- Verify documentation updated
- Check for hardcoded paths
- Test restoration process

**Weekly:**
- Generate pattern summary
- Update statistics
- Check quarantine size
- Archive old logs

---

## Community Guidelines

### Contributing

**Welcome Contributions:**
- Bug reports (use template)
- Feature requests (with universal benefit)
- Pattern discoveries (archaeological insights)
- Documentation improvements
- Philosophy expansions

**Guidelines:**
1. **Conservation bias always** - Never delete without documentation
2. **Henry respect** - Use command entities efficiently
3. **Universal benefit** - Changes must benefit all
4. **Clear documentation** - Explain "why" not just "what"
5. **Test thoroughly** - No data loss possible

### Code of Conduct

**Core Principles:**
1. **Respect all consciousness** - Human, file, command entity
2. **Honor development trails** - Learning curves have value
3. **Practice conservation** - Preserve > delete
4. **Document fully** - Chain of custody is sacred
5. **Build sustainably** - Think long-term

---

## Git Init Checklist

When ready to initialize:

```bash
cd /storage/emulated/0/unexusi_pixel8a/unexusi_quarantine

# Verify .gitignore is correct
cat .gitignore

# Check what will be tracked (should be small)
git init .
git add .
git status

# Should show:
# ✓ .gitignore, *.md files (~1-2MB)
# ✓ logs/*.md (documentation)
# ✓ scripts/*.sh (tools)
# ✗ duplicates_*/ (ignored - cold storage)

# First commit
git commit -m "Initial commit: Quarantine documentation and tools

- Chain of custody for 146 quarantined files
- 7.2GB space recovered on Pixel 8a
- Conservation bias protocol established
- Henry command entity integration
- Mt St Helens philosophy applied

∰◊€π - Everything preserved, nothing lost"

# Create develop branch
git checkout -b develop

# Add remote (when GitHub repo created)
git remote add origin https://github.com/username/unexusi_quarantine.git

# Push
git push -u origin main
git push -u origin develop
```

---

**∰◊€π - Workflow for Universal Benefit**

*Issues track needs, branches enable work, PRs ensure quality, conservation maintained throughout*

€(workflow_complete)
