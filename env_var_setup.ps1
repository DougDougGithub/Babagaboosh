Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$GreetingLabel = New-Object Windows.Forms.Label
$GreetingLabel.Text = "Babagaboosh Env Var Setup"
$GreetingLabel.Font = New-Object Drawing.Font("Arial", 24, [Drawing.FontStyle]::Bold)
$GreetingLabel.AutoSize = $true
$GreetingLabel.Location = New-Object Drawing.Point(10,10)
$GreetingLabel.ForeColor = [System.Drawing.Color]::Black

$AzureApiOutputBox = New-Object System.Windows.Forms.textbox
$AzureApiOutputBox.Text = "AZURE_TTS_KEY"
$AzureApiOutputBox.Multiline = $False
$AzureApiOutputBox.Size = New-Object System.Drawing.Size(200,200)
$AzureApiOutputBox.Location = New-Object Drawing.Point(20,60)

$wshell = New-Object -ComObject Wscript.Shell

$AzureRegionOutputBox = New-Object System.Windows.Forms.textbox
$AzureRegionOutputBox.Text = "AZURE_REGION"
$AzureRegionOutputBox.Multiline = $False
$AzureRegionOutputBox.Size = New-Object System.Drawing.Size(200,200)
$AzureRegionOutputBox.Location = New-Object Drawing.Point(20,100)

$ElevenLabsOutputBox = New-Object System.Windows.Forms.textbox
$ElevenLabsOutputBox.Text = "ELEVENLABS_API_KEY"
$ElevenLabsOutputBox.Multiline = $False
$ElevenLabsOutputBox.Size = New-Object System.Drawing.Size(200,200)
$ElevenLabsOutputBox.Location = New-Object Drawing.Point(20,140)

$OpenAiOutputBox = New-Object System.Windows.Forms.textbox
$OpenAiOutputBox.Text = "OPENAI_API_KEY"
$OpenAiOutputBox.Multiline = $False
$OpenAiOutputBox.Size = New-Object System.Drawing.Size(200,200)
$OpenAiOutputBox.Location = New-Object Drawing.Point(20,180)

$CreateButton = New-Object System.Windows.Forms.Button
$CreateButton.Location = New-Object System.Drawing.Size (200,220)
$CreateButton.Size = New-Object System.Drawing.Size(160,30)
$CreateButton.Font=New-Object System.Drawing.Font("Lucida Console",18,[System.Drawing.FontStyle]::Regular)
$CreateButton.BackColor = "LightGray"
$CreateButton.Text = "Submit"
$CreateButton.Add_Click({
    $AzureApiKey = $AzureApiOutputBox.Text
    $AzureRegion = $AzureRegionOutputBox.Text
    $OpenAiApiKey = $OpenAiOutputBox.Text
    $ElevenLabsApiKey = $ElevenLabsOutputBox.Text

    [Environment]::SetEnvironmentVariable("AZURE_TTS_KEY", $AzureApiKey, [System.EnvironmentVariableTarget]::User)
    [Environment]::SetEnvironmentVariable("AZURE_REGION", $AzureRegion, [System.EnvironmentVariableTarget]::User)
    [Environment]::SetEnvironmentVariable("ELEVENLABS_API_KEY", $ElevenLabsApiKey, [System.EnvironmentVariableTarget]::User)
    [Environment]::SetEnvironmentVariable("OPENAI_API_KEY", $OpenAiApiKey, [System.EnvironmentVariableTarget]::User)
    
    $wshell.Popup("Variables Set",0,"Done",0x1)


})

$ClearButton = New-Object System.Windows.Forms.Button
$ClearButton.Location = New-Object System.Drawing.Size (200,260)
$ClearButton.Size = New-Object System.Drawing.Size(160,30)
$ClearButton.Font=New-Object System.Drawing.Font("Lucida Console",18,[System.Drawing.FontStyle]::Regular)
$ClearButton.BackColor = "LightGray"
$ClearButton.Text = "Clear"
$ClearButton.Add_Click({
    [Environment]::SetEnvironmentVariable("AZURE_TTS_KEY", [NullString]::Value , [System.EnvironmentVariableTarget]::User)
    [Environment]::SetEnvironmentVariable("AZURE_REGION", [NullString]::Value , [System.EnvironmentVariableTarget]::User)
    [Environment]::SetEnvironmentVariable("ELEVENLABS_API_KEY", [NullString]::Value , [System.EnvironmentVariableTarget]::User)
    [Environment]::SetEnvironmentVariable("OPENAI_API_KEY", [NullString]::Value, [System.EnvironmentVariableTarget]::User)

    $wshell.Popup("Variables Cleared",0,"Done",0x1)
})

$Form = New-Object Windows.Forms.Form
$Form.Text = "Babagaboosh Setup Powershell Script"
$Form.Width = 500
$Form.Height = 350
$Form.BackColor = "Gray"

$Form.Controls.Add($GreetingLabel)
$Form.Controls.add($AzureApiOutputBox)
$Form.Controls.add($AzureRegionOutputBox)
$Form.Controls.add($ElevenLabsOutputBox)
$Form.Controls.add($OpenAiOutputBox)
$Form.Controls.add($CreateButton)
$Form.Controls.add($ClearButton)

$Form.Add_Shown({$Form.Activate()})
$Form.ShowDialog()