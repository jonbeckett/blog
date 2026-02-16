#!/bin/bash

# Blog Entry to Journal - Simple Shortcut Creator
# This creates a working Shortcuts file you can import

echo "Creating importable Shortcuts file..."

# Create the shortcut content
cat > "/Users/jonbeckett/Projects/blog/Utils/Process-Blog-Files.shortcut" << 'EOF'
{
  "WFWorkflowActions": [
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.ask",
      "WFWorkflowActionParameters": {
        "WFAskActionPrompt": "Which year would you like to process?",
        "WFInputType": "Text",
        "WFAskActionDefaultAnswer": "2025"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
      "WFWorkflowActionParameters": {
        "WFVariableName": "YearToProcess"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.choosefromlist",
      "WFWorkflowActionParameters": {
        "WFChooseFromListActionPrompt": "What would you like to do?",
        "WFChooseFromListActionSelectMultiple": false,
        "WFChooseFromListItems": [
          "Process all files from year",
          "Select specific files",
          "Process recent files only"
        ]
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
      "WFWorkflowActionParameters": {
        "WFControlFlowMode": 0,
        "WFConditionalActionString": "Process all files from year"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.file.select",
      "WFWorkflowActionParameters": {
        "WFSelectFileMultiple": true,
        "WFFilePickerActionShowFilenames": true
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.filter.files",
      "WFWorkflowActionParameters": {
        "WFContentItemFilter": {
          "Value": {
            "WFActionParameterFilterTemplates": [
              {
                "Property": "File Extension",
                "Operator": 4,
                "Values": {
                  "String": "md"
                }
              }
            ]
          }
        }
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.conditional",
      "WFWorkflowActionParameters": {
        "WFControlFlowMode": 2
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.repeat.each",
      "WFWorkflowActionParameters": {
        "WFControlFlowMode": 0
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.properties.files",
      "WFWorkflowActionParameters": {
        "WFContentItemPropertyName": "Name"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
      "WFWorkflowActionParameters": {
        "WFVariableName": "OriginalFileName"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.gettext",
      "WFWorkflowActionParameters": {}
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
      "WFWorkflowActionParameters": {
        "WFVariableName": "FileContents"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.getvariable",
      "WFWorkflowActionParameters": {
        "WFVariable": "OriginalFileName"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.text.replace",
      "WFWorkflowActionParameters": {
        "WFReplaceTextFind": "\\.md",
        "WFReplaceTextReplace": "",
        "WFReplaceTextRegularExpression": true
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
      "WFWorkflowActionParameters": {
        "WFVariableName": "CleanTitle"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.text",
      "WFWorkflowActionParameters": {
        "WFTextActionText": "📝 Blog Entry\n\n"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.getvariable",
      "WFWorkflowActionParameters": {
        "WFVariable": "FileContents"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.text.combine",
      "WFWorkflowActionParameters": {
        "WFTextSeparator": ""
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.text",
      "WFWorkflowActionParameters": {
        "WFTextActionText": "\n\n---\nMigrated from blog archive"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.text.combine",
      "WFWorkflowActionParameters": {
        "WFTextSeparator": ""
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.setvariable",
      "WFWorkflowActionParameters": {
        "WFVariableName": "FormattedContent"
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.journalentry.create",
      "WFWorkflowActionParameters": {}
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.repeat.each",
      "WFWorkflowActionParameters": {
        "WFControlFlowMode": 2
      }
    },
    {
      "WFWorkflowActionIdentifier": "is.workflow.actions.notification",
      "WFWorkflowActionParameters": {
        "WFNotificationActionTitle": "Migration Complete!",
        "WFNotificationActionBody": "Your blog entries have been added to Journal"
      }
    }
  ],
  "WFWorkflowClientVersion": "2302.0.4",
  "WFWorkflowHasOutputFallback": false,
  "WFWorkflowInputContentItemClasses": [],
  "WFWorkflowMinimumClientVersion": 900,
  "WFWorkflowOutputContentItemClasses": [],
  "WFWorkflowTypes": []
}
EOF

echo "✅ Shortcuts file created: Process-Blog-Files.shortcut"
echo ""
echo "To import this shortcut:"
echo "1. Double-click the .shortcut file"
echo "2. Or open Shortcuts app and use File > Import Shortcut"
echo "3. Or drag the file to the Shortcuts app icon"
echo ""
echo "Note: If the .shortcut file doesn't work, use the URL method below..."

# Create a shareable URL version
echo ""
echo "🔗 Alternative: Use this iCloud sharing URL method"
echo "Visit: https://www.icloud.com/shortcuts/"
echo "Sign in and create a new shortcut manually using the guide in blog-to-journal-shortcuts.md"
EOF

chmod +x "/Users/jonbeckett/Projects/blog/Utils/create-shortcuts-file.sh"

echo "✅ Created Shortcuts file and import script!"
echo ""
echo "Two ways to get the shortcut:"
echo "1. Try double-clicking: Process-Blog-Files.shortcut"
echo "2. Run the import script: ./create-shortcuts-file.sh"
echo ""
echo "If neither works, I'll create a manual step-by-step guide..."