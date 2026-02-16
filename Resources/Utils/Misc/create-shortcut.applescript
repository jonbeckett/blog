#!/usr/bin/env osascript
# AppleScript to create a basic Shortcuts automation
# This creates the shortcut programmatically to avoid signing issues

tell application "Shortcuts Events"
    try
        set newShortcut to make new shortcut with properties {name:"Blog to Journal Migration"}
        
        # Add Ask for Input action
        tell newShortcut
            set inputAction to make new action with properties {identifier:"is.workflow.actions.ask"}
            set inputAction's parameters to {WFAskActionPrompt:"Which year to process? (e.g., 2025)", WFInputType:"Text"}
        end tell
        
        # Add Choose Files action  
        tell newShortcut
            set fileAction to make new action with properties {identifier:"is.workflow.actions.file.select"}
            set fileAction's parameters to {WFSelectFileMultiple:true}
        end tell
        
        # Add Filter Files action
        tell newShortcut
            set filterAction to make new action with properties {identifier:"is.workflow.actions.filter.files"}
            set filterAction's parameters to {WFContentItemFilter:{WFActionParameterFilterTemplates:{{Property:"File Extension", Operator:4, Values:{String:"md"}}}}}
        end tell
        
        # Add Repeat action
        tell newShortcut
            set repeatAction to make new action with properties {identifier:"is.workflow.actions.repeat.each"}
        end tell
        
        # Add Get Text from File action
        tell newShortcut
            set textAction to make new action with properties {identifier:"is.workflow.actions.gettext"}
        end tell
        
        # Add Text formatting action
        tell newShortcut
            set formatAction to make new action with properties {identifier:"is.workflow.actions.text"}
            set formatAction's parameters to {WFTextActionText:"📝 Blog Entry\n\n[Previous Output]\n\n---\nMigrated from blog archive"}
        end tell
        
        # Add Copy to Clipboard action
        tell newShortcut
            set clipAction to make new action with properties {identifier:"is.workflow.actions.setclipboard"}
        end tell
        
        # Add notification
        tell newShortcut
            set notifyAction to make new action with properties {identifier:"is.workflow.actions.notification"}
            set notifyAction's parameters to {WFNotificationActionTitle:"Entry Ready", WFNotificationActionBody:"Blog entry copied to clipboard - paste into Journal"}
        end tell
        
        display dialog "Shortcut 'Blog to Journal Migration' created successfully!" buttons {"OK"} default button "OK"
        
    on error errMsg
        display dialog "Error creating shortcut: " & errMsg buttons {"OK"} default button "OK"
    end try
end tell